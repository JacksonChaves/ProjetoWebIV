

<form class="crud" on:submit|preventDefault={sendForm}>
    <input type="text" id="name" name="name" placeholder="teste" required autocomplete="off">
    
    <input type="submit" value="buscar">
</form>




<script>

    let artistas = [];
    let promise = sendForm();
    async function sendForm(){
        
       
        const name = document.getElementById("name").value;
        
        const res = await fetch(`http://localhost:8000/get_artista/${name}`);
        
        const json = await res.json();
        artistas = json;
        
        console.log(name)
        
       
    }
    

    async function favoritarArtista(name, tmdb_id, rank) {
		const res = await fetch(`http://localhost:8000/fav_artista/`, {
			method: 'POST',
			headers: {
			'Content-Type': 'application/json'
			},
			body: JSON.stringify({ name: name.toString(), tmdb_id:tmdb_id.toString(), rank:rank.toString(),user_id: "1"})
	});
    if (res.ok) {
			alert('Artista adicionado aos favoritos com sucesso!');
		} else {
			alert('Erro ao adicionar artista aos favoritos.');
		}
	}

</script>

{#if artistas.length > 0}
    <h1>Lista de artistas</h1>
    {#each artistas as artista}
        <p>ID: {artista.id}</p>
        <p>Nome do Artista: {artista.name}</p>
        <p>Rank: {artista.rank}</p>
        <img src="{artista.image}" alt="">
        <p>Biografia em Inglês: {artista.biography}</p>
        
        <p>Data de Nascimento: {artista.birthday}</p>
        <button type="button" on:click={() => favoritarArtista(artista.id, artista.name, artista.rank)}>Adicionar a favoritos</button>

        <br>
    {/each}
{:else}
    <p>Nenhum artista encontrado.</p>
{/if}
  




