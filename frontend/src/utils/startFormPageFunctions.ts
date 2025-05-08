import { apiPost } from "./api";

export async function sendInitFeelingsText(text : string){
    
    const answer = await apiPost(
        '/next-form',
        {
            text_data: text,
        }
    );
    const data = answer.data;
    return data;
}
