<script>
  // let favoritos = "";
  let promise = getFavoritos();
  async function getFavoritos() {
    const res = await fetch(`http://localhost:8000/favoritos?user_id=1`);
    const text = await res.json();
    var filmes = [];
    text.forEach(async(element) =>  {
      const fav = await fetch(`http://localhost:8000/filmes/` + element.title)
      filmes.push(await fav.json());
    });

    if (res.ok)
      { 
        console.log(filmes)
        return text; 
      } 
  
	  else { throw new Error(text);}
	  }
    
    async function deleteFavorito(e) {
		e.preventDefault();
		// const userId = e.target.elements.id.value;
		const tmdb_id = e.target.elements.tmdb_id.value;

		const res = await fetch(`http://localhost:8000/favoritos/${tmdb_id}`, {
			method: 'DELETE',
			headers: {'Content-Type': 'application/json'}
		});

		if (res.ok) {
			resposta = `Filme ${userName} desfavoritado`;
			promise = deleteFavorito();
		}
	  }
  

</script>

{#await promise}
  
<!-- <button on:click={handleClick}> Carregar filmes favoritos... </button> -->
  
{:then favoritos}
  <h1>Meus Filmes Favoritos</h1>
  {#each favoritos as favorito}
    <!-- <p>{favorito.user_id}</p> -->
    <p>Nome: {favorito.title} - Id: {favorito.tmdb_id} </p>
    <form on:submit|preventDefault={deleteFavorito}>
			<input type="hidden" name="id" value="{favorito.id}">
			<input type="hidden" name="tmdb_id" value="{favorito.tmdb_id}">
			<button type="submit">Desfavoritar</button>
		</form>
  {/each}

{/await}