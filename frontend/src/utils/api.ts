const API_URL = 'https://your-api-url.com'; // Replace with your actual API URL

export interface APIResponse<T = unknown> {
    success: boolean;
    message: string;
    data?: T; // Optional data field to hold the response data
}




export const apiGet = async <T>(endpoint: string): Promise<APIResponse<T>> => {
    try {
        const response = await fetch(`${API_URL}${endpoint}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return { success: true, message: 'Data retrieved successfully', data };
    } catch (error) {
        console.error('Error during GET request:', error);
        throw error;
    }
};

export const apiPost = async <T,K>(endpoint: string, data: T): Promise<APIResponse<K>> => {
    try {
        const response = await fetch(`${API_URL}${endpoint}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const responseData = await response.json();
        return { success: true, message: 'Data posted successfully', data: responseData };
    } catch (error) {
        console.error('Error during POST request:', error);
        throw error;
    }
};

export const apiPut = async <T,K>(endpoint: string, data: T): Promise<APIResponse<K>> => {
    try {
        const response = await fetch(`${API_URL}${endpoint}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const responseData = await response.json();
        return { success: true, message: 'Data updated successfully', data: responseData };
    } catch (error) {
        console.error('Error during PUT request:', error);
        throw error;
    }
};

export const apiDelete = async (endpoint: string): Promise<APIResponse<null>> => {
    try {
        const response = await fetch(`${API_URL}${endpoint}`, {
            method: 'DELETE',
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return { success: true, message: 'Data deleted successfully', data: null };
    } catch (error) {
        console.error('Error during DELETE request:', error);
        throw error;
    }
};
