import { apiPost } from "./api";

export async function getDiagnosis(initText : string, formData){
    
    const answer = await apiPost(
        '/fetch-diagnosis',
        {
            text_data: initText,
            questions_data : formData
        }
    );
    const data = answer.data;
    return data
}
