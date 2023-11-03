<script>
  let favoritos = [];
  let promise = getFavoritos();
  async function getFavoritos() {
    const res = await fetch(`http://localhost:8000/favoritos/1`);
    if (res.ok) {
      favoritos = await res.json();
    } else {
        console.error('Falha ao obter favoritos.');
    }
    
  }

</script>

<h1>Meus Filmes Favoritos</h1>
<!-- <main> -->
  <!-- svelte-ignore missing-declaration -->
{#await promise}

  <p>Carregando favoritos...</p>
  
  {:then}
  {#if favoritos.length > 0}
    <ul>
      {#each favoritos as favorito}
      <p>{favorito.title}</p>
      <img src="{favorito.image}" alt="">
      {/each}
    </ul>
  {:else}
    <p>Nenhum filme favoritado ainda.</p>
  {/if}
{/await}
<!-- </main> -->