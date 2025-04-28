import { FormData, FormReponse } from "./data";
import { apiGet, apiPost } from "./api";

export async function sendForm(formData: FormReponse) {

   const response = await apiPost<FormReponse,null>('/form', formData);

}

export async function getFirstForm(): Promise<FormData|undefined> {
    const response = await apiGet<FormData>('/form');
    return response.data;
}

export async function getFormByResponses(formData: FormReponse): Promise<FormData|undefined> {
    const response = await apiPost<FormReponse,FormData>('/form-ai', formData);
    return response.data;
}
