import React, { useState } from "react";
import { addToFavorites, removeFromFavorites } from "static/js/api.js";

const FavoriteButton = ({ eventId, isFavorite, token }) => {
    const [favorite, setFavorite] = useState(isFavorite);

    const handleFavorite = async () => {
        try {
            if (favorite) {
                await removeFromFavorites(eventId, token);
            } else {
                await addToFavorites(eventId, token);
            }
            setFavorite(!favorite);
        } catch (error) {
            console.error("Error updating favorites", error);
        }
    };

    return (
        <button onClick={handleFavorite} className="btn btn-primary">
            {favorite ? "Remove from Favorites" : "Add to Favorites"}
        </button>
    );
};

export default FavoriteButton;
