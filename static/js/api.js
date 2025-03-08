import axios from "axios";

const API_URL = "http://localhost:8000/api";

export const addToFavorites = async (eventId, token) => {
    return await axios.post(
        `${API_URL}/favorites/add/${eventId}/`,
        {},
        { headers: { Authorization: `Bearer ${token}` } }
    );
};

export const removeFromFavorites = async (eventId, token) => {
    return await axios.delete(
        `${API_URL}/favorites/remove/${eventId}/`,
        { headers: { Authorization: `Bearer ${token}` } }
    );
};
