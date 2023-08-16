function deleteRecipe(recipeId) {
    fetch('/delete-recipe', {
        method: 'POST',
        body: JSON.stringify({ recipeId: recipeId }),
    }).then((_res) => {
        window.location.href ="/recipes";
    });
}

function updateRecipe(recipeId) {
   // fetch('/update-recipe',{
   //     method: 'POST',
   //     body: JSON.stringify({ recipeId: recipeId}),
   // }).then((_res) => {
   //     window.location.href = "/recipes";
   // });
}


const updateModal = document.getElementById('updateModal')
if (updateModal) {
    console.log('whatever, I made it in.');
    updateModal.addEventListener('show.bs.modal', event => {
        const button = event.relatedTarget
        const recipeUpdate = button.getAttribute('data-bs-whatever')
        const updateTitle = updateModal.querySelector('.modal-title')
        const modalBodyInput = updateModal.querySelector('.modal-body input')
        updateTitle.textContent = `Update to ${recipeUpdate}`
        modalBodyInput.value = recipeUpdate
 })
}
