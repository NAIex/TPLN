export enum FormQuestionType {
    SHORT_ANSWER = "SHORT_ANSWER",
    NONE = "NONE",
}
export interface FormQuestionProps {
    id: number;
    type: FormQuestionType;
    question?: string;
    description?: string;
    isRequired: boolean;
    shortAnswer?: string;
    appear: boolean;
    onTrigger?: () => void;
    trigger?: boolean;
}