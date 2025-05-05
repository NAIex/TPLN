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
    is_critical?: boolean;
}


export interface FormQuestionAnswer {
    is_critical:boolean;
    score_contribution:number;
    text:string;
}
export interface FormQuestionObject{
    answer: string|null;
    is_critical:boolean;
    text:string;

}