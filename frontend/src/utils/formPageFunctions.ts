import { FormData, FormReponse } from "./data";
import { apiGet, apiPost } from "./api";

export interface FormStructure{
    form_section : string;
    items : {
        question_id : number;

        answer_options : [string];
        is_critical : boolean;
        text : string;
        timeframe : string;

    }
}

export interface FormResponse{
    
    [form_section : string] : boolean | [boolean] | string;
    
}

export async function sendForm(initText : string, formData: FormReponse){
    
    const answer = await apiPost(
        '/next-form',
        {
            text_data: initText,
            questions_data : formData
        }
    );
    const data = answer.data;
    return data
}



export async function getFirstForm(): Promise<FormData|undefined> {
    const response = await apiGet<FormData>('/form');
    return response.data;
}

export async function getFormByResponses(formData: FormReponse): Promise<FormData|undefined> {
    const response = await apiPost<FormReponse,FormData>('/form-ai', formData);
    return response.data;
}
