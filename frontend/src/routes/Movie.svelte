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
			alert('Erro ao adicionar filme aos favoritos.');
		}
	 }
	  
  </script>
  
  <button on:click={handleClick}> Carregar filmes... </button>
  
  <!-- svelte-ignore missing-declaration -->
  {#await promise}
	  <p>...loading</p>
  {:then filmes}
	<h1>Lista de filmes</h1>
	{#each filmes as filme}
		<p>{filme.title}</p>
		<img src="{filme.image}" alt="">
		<button type="button" on:click={() => favoritarFilme(filme.id, filme.title)}>Adicionar a favoritos</button>
	{/each}
	<!-- <p>{filmes.title}</p> -->
  {:catch error}
	  <p style="color: red">{error.message}</p>
  {/await}
  



















  
