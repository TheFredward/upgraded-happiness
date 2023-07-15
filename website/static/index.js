function deleteRecipe(recipeId) {
    fetch('/delete-recipe', {
        method: 'POST',
        body: JSON.stringify({ recipeId: recipeId }),
    }).then((_res) => {
        window.location.href ="/recipes";
    });
}

function updateRecipe(recipeId) {
    fetch('/update-recipe',{
        method: 'POST',
        body: JSON.stringify({ recipeId: recipeId}),
    }).then((_res) => {
        window.location.href = "/recipes";
    });
}
