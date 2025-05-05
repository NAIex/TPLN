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
    trigger?: boolean;
    is_critical?: boolean;


    onTrigger?: () => void;
    onChangeText?: (text: string) => void;
    onChangeBool?: (value: boolean) => void;
}


export interface FormQuestionAnswer {
    is_critical:boolean;
    score_contribution:number;
    text:string;
}
export interface FormQuestionObject{
    text_answer: string|null;
    bool_answer: boolean|null;
    is_critical:boolean;
    text:string;


}