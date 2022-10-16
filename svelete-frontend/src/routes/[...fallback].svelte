<script>
  import SideMenu from "$components/SideMenu.svelte";
  import { IonGrid } from "@ionic/core/components/ion-grid";
  import "../theme/tailwind.css";
  var FordPrefectQuotes = [
    `How would you react if I said that I'm not from Guildford at all, but from a small planet somewhere in the vicinity of Betelgeuse?`,
    `“Funny,” he intoned funereally, “how just when you think life can’t possibly get any worse it suddenly does.”`
  ];
</script>

<SideMenu title="Page not found" />
<ion-content id="router-content">
  <div class="w-full h-full flex flex-col align-center justify-center px-20 sm-w:px-10">
    <span class="text-center font-bold  text-4xl">420</span>
    <span class="text-center">Page Not Found 😿</span>
    <span class="text-center text-xs my-5">{FordPrefectQuotes[0]}</span>
  </div>
</ion-content>