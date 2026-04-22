import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000/api/v1',
});

export const uploadReport = async (brandName: string, file: File) => {
    const formData = new FormData();
    formData.append('file', file);

    // Note: We send brand_name as a query param or form data depending on backend config
    const response = await api.post(`/upload?brand_name=${encodeURIComponent(brandName)}`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
    });
    return response.data;
};