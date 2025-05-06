from classes.questions.data import questions_by_subscale

FIRST_TEXT_QUESTION: str = "Scrie câteva rânduri despre tine: cine ești, ce îți place și ce te motivează."
THRESHOLD: float = 0.3

def get_subscale_weights(texts: dict[str, str], excluded_subscales: list[str]) -> dict[str, float]:
	from transformers import pipeline
	import logging
	logging.getLogger("transformers").setLevel(logging.ERROR)
	classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
	premise = "".join(f"{q}\n{a}\n\n" for q, a in texts.items())
	def hypothesis_from_subscale(subscale: str): return f"Această persoană suferă de {subscale}"
	subscales = questions_by_subscale.keys()
	subscales_without_excluded = list(filter(lambda subscale: subscale not in excluded_subscales, subscales))
	if len(subscales_without_excluded) == 0: return {}
	result = classifier(premise, list(map(hypothesis_from_subscale, subscales_without_excluded)), multi_label=True)
	scores = {subscale: score for subscale, score in zip(subscales_without_excluded, result["scores"])}
	return scores

def select_next_subscale(first_text: str, answers_by_subscale: dict[str, dict[int, bool | list[bool] | str]]) -> str | None:
	texts: dict[str, str] = {FIRST_TEXT_QUESTION: first_text} | {
		q: a for _, qs in answers_by_subscale.items() for q, a in qs.items() if isinstance(a, str)
	}
	subscales_to_exclude = list(filter(lambda kvp: len(kvp[1]) > 0, answers_by_subscale))
	weights_of_subscales = get_subscale_weights(texts, subscales_to_exclude)
	if len(weights_of_subscales) == 0: return None
	# for k, v in weights_of_subscales.items():
	# 	print(f"{k} => {v}")
	max_subscale = max(weights_of_subscales, key=weights_of_subscales.get)
	return max_subscale if weights_of_subscales[max_subscale] >= THRESHOLD else None
