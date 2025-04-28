export interface FormData {
    id            : number;
    formName      : string;
    formQuestions : [string];
}

export interface FormReponse{
    id                  : number;
    formName            : string;
    formQuestionResponse: [FormQuestionResponse];
}
export interface FormQuestionResponse{
    question : string;
    response :boolean;
    details? :string;
}
