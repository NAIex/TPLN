from classes.questions.data import questions_by_subscale

FIRST_TEXT_QUESTION: str = ""

################################################ THIS NEEDS TO BE CHANGED ################################################
def get_subscale_weights(texts: dict[str, str], excluded_subscales: list[str]) -> dict[str, float]:
    return {subscale: 1 / len(qs) for subscale, qs in questions_by_subscale.items() if subscale not in excluded_subscales}
################################################ THIS NEEDS TO BE CHANGED ################################################

def select_next_subscale(first_text: str, answers: dict[str, dict[int, bool | list[bool] | str]]):
    texts = {FIRST_TEXT_QUESTION: first_text} | {
        q: a for _, qs in answers.items() for q, a in qs.items() if isinstance(a, str)
    }
    subscales_to_exclude = list(filter(lambda k, v: len(v) > 0, answers))
    weights = get_subscale_weights(texts)
    # for k, v in weights.items():
    #     print(f"{k} => {v}")
    return max(weights, key=weights.get)
