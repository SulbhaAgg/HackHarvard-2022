<script>
  import SideMenu from "$components/SideMenu.svelte";
  import { IonGrid } from "@ionic/core/components/ion-grid";
  import FaSolidCamera from "svelte-icons-pack/fa/FaSolidCamera";
  import { onMount } from 'svelte';
  import "../theme/tailwind.css";
  import Icon from "svelte-icons-pack";
  var serverURL = 
  //'http://127.0.0.1:5000'
  'https://perfect-fit-production.up.railway.app';
  let cardPoints=[];
  let cardPoints2=[];
  let lines=[];
  let picContainer = null
  let video = null;
  let canvas = null;
  let screenshotImage = null;
  let imgElements = null;
  let camButton = null;
  let pixelCanvas = null;
  let resultDiv = null;
  var videoDevice;
  let beginPointSelection = "false";
  let clotheDropdown = null;
  let selectedType = "None";
  let size = "N/A"
  let message = "We're sorry for some reason we couldn't retrieve data for you 😥. Feel free to check back later ⌛"
  const constraints = {
        video: {
          width: {
            min: 1280,
            ideal: 1080,
            max: 2560,
          },
          height: {
            min: 720,
            ideal: 1920,
            max: 1440
          },
          facingMode: 'user'
        }
  }
  const getCameraSelection = async () => {
    const devices = await navigator.mediaDevices.enumerateDevices();
    const videoDevices = devices.filter(device => device.kind === 'videoinput');
    videoDevice = videoDevices[0].deviceId;
  };
  const handleStream = (stream) => {
  video.srcObject = stream;
  };
  const startStream = async (constraints) => {
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleStream(stream);
  };
  onMount(()=>{
    getCameraSelection();
    if ('mediaDevices' in navigator && navigator.mediaDevices.getUserMedia) {
      const updatedConstraints = {
        ...constraints,
        deviceId: {
          exact: videoDevice
        }
      };
      startStream(updatedConstraints);
    }
  })
  const doScreenshot = () => {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    let ratio = video.videoWidth/video.videoHeight;
    video.classList.add("hidden");
    camButton.classList.add("hidden");
    canvas.getContext('2d').drawImage(video, 0, 0);
    screenshotImage.src = canvas.toDataURL('image/webp');
    //screenshotImage.classList.remove('hidden');
    //pixelCanvas.classList.add(`aspect-[${video.videoHeight}/${video.videoWidth}]`);
    pixelCanvas.height=video.videoHeight;
    //pixelCanvas.classList.remove('hidden');
    imgElements.classList.remove('hidden');
    canvas.classList.remove('hidden');
    beginPointSelection="card";
    
  };

  const SendData = async ()=>{
    console.log("Sending data...")
    while(lines.length<4){
      lines.push([0])
      lines=lines;
    }
    var req = JSON.stringify({
          type: selectedType,
          cardpoints1: cardPoints,
          cardpoints2: (cardPoints2.length>0)?cardPoints2:[0],
          lines: lines,
        });
    console.log(req);

    try{
      var res = await fetch(serverURL+"/post_data",{
         headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
          },
        method:"PUT",
        body:req
      })
      var data = await res.json()
      console.log(data);
      if(res.status==200 && data.size!='') {
        size =''
        if(selectedType=="bra") size += data.extra;
        size += data.size;
        message = "We hope this advice will help you get the clothes that fit your body, so you feel good about being... well you 😊";}
      setTimeout(()=>{
         resultDiv.classList.remove("hidden");
         resultDiv.classList.add('flex');
            screenshotImage.classList.add('hidden');
            //pixelCanvas.classList.add(`aspect-[${video.videoHeight}/${video.videoWidth}]`);
            pixelCanvas.classList.add('hidden');
            imgElements.classList.add('hidden');
          },1000)

    }
    catch(error){
      console.log("Error: ", error)
    }
  }

  let lineNum = 0;
  let picNum =0;
  let currLine = 0;
  const selectPoints= (e)=>{
    if(beginPointSelection=="false" || selectedType=='None')return;
    const rect = canvas.getBoundingClientRect()
    const x = e.clientX - rect.left
    const y = e.clientY - rect.top
    var ctx = canvas.getContext("2d");
    if(beginPointSelection=="card"){
      ctx.fillStyle="#00aa77"
      ctx.strokeStyle = 'green';
      ctx.lineWidth = 5;
      ctx.beginPath();
      if(cardPoints.length<4){
        cardPoints.push([x,y]);
        cardPoints=cardPoints;
        if(cardPoints.length>1){
          var prevPoint = cardPoints[cardPoints.length-2];
          ctx.moveTo(prevPoint[0], prevPoint[1]);
          ctx.lineTo(x,y);
          ctx.stroke();     
        }
        if(cardPoints.length>=4){
          var nxtPoint = cardPoints[0];
          ctx.moveTo(x,y);
          ctx.lineTo(nxtPoint[0], nxtPoint[1]);
          ctx.stroke();
          console.log(cardPoints);
          beginPointSelection="line1";
        }
      }
      else{
        cardPoints2.push([x,y]);
        cardPoints2=cardPoints2;
        if(cardPoints2.length>1){
          var prevPoint = cardPoints2[cardPoints2.length-2];
          ctx.moveTo(prevPoint[0], prevPoint[1]);
          ctx.lineTo(x,y);
          ctx.stroke();     
        }
        if(cardPoints2.length>=4){
          console.log(cardPoints2);
          var nxtPoint = cardPoints2[0];
          beginPointSelection="line2"
          ctx.moveTo(x,y);
          ctx.lineTo(nxtPoint[0], nxtPoint[1]);
          ctx.stroke();
        }
      }
    }
    else if(beginPointSelection.includes("line")){
      ctx.fillStyle = '#ff0000';
      if(currLine==lines.length){
        lines.push([[x,y]]);
        
      }
      else{
        console.log(currLine)
        lines[lines.length-1].push([x,y]);
        lines=lines;
        console.log(lines[lines.length-1]);
        currLine++;
        ctx.strokeStyle = 'red';
        ctx.lineWidth = 5;
        ctx.beginPath();
        var prev=lines[lines.length-1][0]
        ctx.moveTo(prev[0], prev[1])
        ctx.lineTo(x,y);
        ctx.stroke();
        if(selectedType=="t-shirt" && currLine>=2){
          beginPointSelection="false";
          SendData();
        }
        else if(selectedType=="bra" && currLine >=4){
          beginPointSelection="false";
          SendData();
        }
        else if(selectedType=="pants" && currLine>=2){
          beginPointSelection="false"
          SendData();
        }
        else if(((currLine%2===0) || (selectedType=="pants")) && currLine!=0){
          setTimeout(()=>{
            video.classList.remove("hidden");
            camButton.classList.remove("hidden");
            screenshotImage.classList.add('hidden');
            //pixelCanvas.classList.add(`aspect-[${video.videoHeight}/${video.videoWidth}]`);
            pixelCanvas.classList.add('hidden');
            imgElements.classList.add('hidden');

          },1000)
        }
      }
    }
    ctx.fillRect(x-5,y-5, 10, 10);
  }
  const selectClothe =()=>{
    selectedType= clotheDropdown.value;
    beginPointSelection="card"
    console.log(beginPointSelection);
  }

</script>

<SideMenu title="PerfectFit" />
<ion-content id="router-content">
  <div class="fixed w-20 h-32 bg-gray-500">
    <div class="text-bold">TIPS</div>
  </div>
  <div class="w-full h-full relative bg-gray-900 d-flex">
    <div class="w-full h-full flex-col absolute hidden bg-gray-900 justify-center items-center" bind:this={resultDiv}>
      <div class="text-xl">The best {selectedType} size for you is: {size}</div>
      <div>{message}</div>
    </div>
    <div class="w-full h-full absolute hidden" bind:this={imgElements}>
      <div>
        <ion-title>Clothes Selection</ion-title>
        <ion-list>
          <ion-item>
            <ion-select placeholder="Select clothe to mesure" bind:this={clotheDropdown} on:ionChange={(e)=>selectClothe()}>
              <ion-select-option value="t-shirt">T-Shirt</ion-select-option>
              <ion-select-option value="pants">Pants</ion-select-option>
              <ion-select-option value="bra">Bra</ion-select-option>
            </ion-select>
          </ion-item>
        </ion-list>
      </div>
      <canvas class="absolute hidden" bind:this={canvas} on:mousedown={(e)=>selectPoints(e)}></canvas>
      <canvas class="absolute hidden z-[99] w-[40rem]" bind:this={pixelCanvas} on:mousedown={(e)=>selectPoints(e)}></canvas>
      <div class="w-full h-auto" bind:this={picContainer}>
        <img class="absolute hidden w-[40rem]" alt="" bind:this={screenshotImage} on:mousedown={(e)=>selectPoints(e)} draggable={false}>
      </div>
    </div>
    <video class={`absolute w-full h-full z-0`} bind:this={video} autoplay></video>
    <div class="absolute w-full h-full flex justify-center items-end p-2" bind:this={camButton}>
      <button class="w-32 h-32 rounded-full bg-white flex justify-center items-center"
        on:click|stopPropagation={(e)=>doScreenshot()}
        bind:this={camButton}
      >
        <Icon src={FaSolidCamera} size="64"/>
      </button>
    </div>
  </div>
</ion-content>
