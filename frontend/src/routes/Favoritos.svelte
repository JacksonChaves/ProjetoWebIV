<script>
  let resposta = "";
  let promise = getFavoritos();
  async function getFavoritos() {
    const res = await fetch(`http://localhost:8000/favoritos?user_id=1`);
    const text = await res.json();
    var filmes = [];
    text.forEach(async(favorito) =>  {
      const fav = await fetch(`http://localhost:8000/filmes/` + favorito.title)
      filmes.push(await fav.json());
    });

    if (res.ok)
      { 
        console.log(filmes)
        return text; 
      } 
  
	  else { throw new Error(text);}
	  }
    function handleClick() {
		  promise = getFavoritos();
	  }
    
    async function deleteFavorito(e) {
		e.preventDefault();
		const title = e.target.elements.title.value;
		const tmdb_id = e.target.elements.tmdb_id.value;

		const res = await fetch(`http://localhost:8000/favoritos/${tmdb_id}`, {
			method: 'DELETE',
			headers: {'Content-Type': 'application/json'}
		});

		if (res.ok) {
			resposta = `Filme ${title} desfavoritado`;
			promise = getFavoritos();
		}
	  }
  

</script>
<button on:click={handleClick}> Carregar filmes favoritos... </button>

{#await promise}
  <p>...loading</p>
{:then favoritos}
  <h1>Meus Filmes Favoritos</h1>
  {#each favoritos as favorito}
    <!-- <p>{favorito.user_id}</p> -->
    <p>Nome: {favorito.title} - Id: {favorito.tmdb_id} </p>
    <form on:submit|preventDefault={deleteFavorito}>
			<input type="hidden" name="id" value="{favorito.id}">
			<input type="hidden" name="tmdb_id" value="{favorito.tmdb_id}">
      <input type="hidden" name="title" value="{favorito.title}">
      <br>
			<button type="submit">Desfavoritar</button>
		</form>
  {/each}

{/await}