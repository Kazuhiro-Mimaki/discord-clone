<script lang="ts">
import { defineComponent, reactive, ref } from "vue";
import { io } from "socket.io-client";

export default defineComponent({
  setup() {
    const count = ref(0);
    const socket = io("http://localhost:8000");

    socket.on("connect", () => {
      console.log("successfully connected with socket.io server");
      console.log(socket.id);
    });
    socket.on("response", () => {
      console.log("Response", socket.id);
    });
    socket.on("message", (data) => {
      console.log(data);
    });

    return {
      count,
    };
  },
});
</script>

<template>
  <div>
    <span>{{ count }}</span>
    <button @click="count++">Increment count</button>
  </div>
</template>
