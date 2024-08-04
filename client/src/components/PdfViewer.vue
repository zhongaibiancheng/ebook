<template>
    <v-container>
    	<div id="flipbookContainer"></div>
    	<button @click="openPdf">Click me</button>
    </v-container>
</template>

<script>
import { ref, onMounted } from 'vue';
import options from '../utils/const.ts';

export default {
  name: 'PdfViewer',
  setup() {
    onMounted(() => {
    	// let options_df_button = options;
    	// window.option_df_button = options_df_button;
    	// console.log(window.option_df_button);
    });

    const openPdf=()=>{
    	console.log("open pdf ********");
    	const pdf = "/books/intro.pdf";
    	$("#flipbookContainer").flipBook(pdf, options);
    }
    return {
openPdf
    };
  },
};
</script>