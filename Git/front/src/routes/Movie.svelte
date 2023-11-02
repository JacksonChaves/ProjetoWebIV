<script>
	  let promise = getFilmes();
	  async function getFilmes() {
	  // faz um request GET para endpoint /filmes
		const res = await fetch(`http://localhost:8000/filmes`);
		const text = await res.json();
		if (res.ok) { return text; } 
	  	else { throw new Error(text);}
	  }
	  function handleClick() {
		promise = getFilmes();
	  }

	  async function favoritarFilme(tmdbId) {
		const res = await fetch(`http://localhost:8000/favoritos/`, {
			method: 'POST',
			headers: {
			'Content-Type': 'application/json'
			},
			body: JSON.stringify({ user_id: 1, tmdb_id: tmdbId })
		});

		if (res.ok) {
			// Reload the list of favorite movies when a movie is added to favorites
			handleFetchFavoritos();
			console.log('Filme adicionado aos favoritos com sucesso!');
		} else {
			console.error('Erro ao adicionar filme aos favoritos.');
		}
	 }
	  
  </script>
  
  <button on:click={handleClick}> Carregar filmes... </button>
  
  {#await promise}
	  <p>...loading</p>
  {:then filmes}
	<h1>Lista de filmes</h1>
	{#each filmes as filme}
		<p>{filme.title}</p>
		<img src="{filme.image}" alt="">
		<button type="button" on:click={() => favoritarFilme(filme.tmdb_id)}>Adicionar a favoritos</button>
	{/each}
	<p>{filmes.title}</p>
  {:catch error}
	  <p style="color: red">{error.message}</p>
  {/await}
  

  <!--
	Implementar o componente Artista.svelte
	-exibir a bio do artista
  -->


















  