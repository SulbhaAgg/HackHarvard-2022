<script lang="ts">
    type users ={
        id: string;
        name: string;
    }
    export let users;
</script>
<ion-list>
  <ion-list-header>Random User People</ion-list-header>
  {#each users as user (user.id)}
    <ion-item>
      <ion-avatar slot="start">
        <img
          alt="primagen avatar"
          src="https://yt3.ggpht.com/ytc/AKedOLTFxJUOhj2kZJMjmfUhCeSItIwk4wGndF7oJAt4=s900-c-k-c0x00ffffff-no-rj"
        />
      </ion-avatar>
      <ion-label>
        <h2>{user.name}</h2>
        <p>User</p>
      </ion-label>
    </ion-item>
  {/each}
</ion-list>
