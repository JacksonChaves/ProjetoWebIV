<script>
  let favoritos = [];

  // Function to fetch favorite movies
  async function handleFetchFavoritos() {
    const res = await fetch(`http://localhost:8000/favoritos/1`); // Replace with the correct endpoint
    if (res.ok) {
      favoritos = await res.json();
    }
  }

  // Fetch favorite movies when the component loads
  onMount(() => {
    handleFetchFavoritos();
  });
</script>

<main>
  <h1>Meus Filmes Favoritos</h1>

  {#if favoritos.length > 0}
    <ul>
      {#each favoritos as favorito (favorito.tmdb_id)}
        <li>{favorito.title}</li>
      {/each}
    </ul>
  {:else}
    <p>Nenhum filme favoritado ainda.</p>
  {/if}
</main>