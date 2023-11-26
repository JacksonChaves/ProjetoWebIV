

<form class="crud" on:submit|preventDefault={sendForm}>
    <input type="text" id="title" name="title" placeholder="Título do Filme" required autocomplete="off">
    
    <input type="submit" value="buscar">
</form>




<script>

    let filmes = [];
    let promise = sendForm();
    async function sendForm(){
        
       
        const title = document.getElementById("title").value;
        
        const res = await fetch(`http://localhost:8000/filmes/${title}`);
        
        const json = await res.json();
        filmes = json;
        
        console.log(title)
        
       
    }
    

    async function favoritarFilme(tmdbId, title) {
		const res = await fetch(`http://localhost:8000/favoritos/`, {
			method: 'POST',
			headers: {
			'Content-Type': 'application/json'
			},
			body: JSON.stringify({ user_id: "1", tmdb_id: tmdbId.toString(), title: title})
		});

		if (res.ok) {
			alert('Filme adicionado aos favoritos com sucesso!');
		} else {
			alert('Este filme já está adicionado aos favoritos, sua anta!');
		}
	 }

</script>

{#if filmes.length > 0}
    <h1>Lista dos Filmes</h1>
    {#each filmes as filme}
        <p>Nome do Filme: {filme.title}</p>
        <p>ID do Filme: {filme.id}</p>
        <img src="{filme.image}" alt="">
        <br>
        <button type="button" on:click={() => favoritarFilme(filme.id, filme.title)}>Adicionar a favoritos</button>
        <br>
    {/each}
{:else}
    <p>Nenhum filme encontrado.</p>
{/if}
  




