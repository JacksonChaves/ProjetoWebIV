<script>
    import Artista from "./Artista.svelte";

 

    let resposta = "";
    let promise = getArtistas();
    async function getArtistas() {
    // faz um request GET para endpoint /Users
      const res = await fetch(`http://localhost:8000/fav_artista`);
      const text = await res.json();
      if (res.ok) { return text; } 
        else { throw new Error(text);}
    }
    function handleClick() {
      promise = getArtistas();
    }
    
    

    async function deleteArtista(e) {
		e.preventDefault();
		const name = e.target.elements.name.value;
		const tmdb_id = e.target.elements.tmdb_id.value;

		const res = await fetch(`http://localhost:8000/fav_artista/${tmdb_id}`, {
			method: 'DELETE',
			headers: {'Content-Type': 'application/json'}
		});

		if (res.ok) {
			resposta = `Artista ${name} desfavoritado`;
			promise = getArtistas();
		}
	  }

  

</script>

<button on:click={handleClick}> Carregar Artistas </button>

{#await promise}
  <p>...loading</p>
{:then artistas}
  <h1>Lista de Artistas</h1>
  {#each artistas as artista}
      <p>ID: {artista.tmdb_id} - Nome: {artista.name} - Rank: {artista.rank}</p>
      
      <form on:submit|preventDefault={deleteArtista}>
        <input type="hidden" name="name" value="{artista.name}">
        <input type="hidden" name="tmdb_id" value="{artista.tmdb_id}">
        
        <button type="submit">Desfavoritar</button>
    </form>
      
      
  {/each}

{:catch error}
    <p style="color: red">{error.message}</p>
{/await}