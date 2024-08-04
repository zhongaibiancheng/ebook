import { defineStore } from 'pinia'

export const useCommon = defineStore('common', {
  state: () => ({
    /** @type {boolean} */
    login:false,
  }),
  getters: {//computed 
   
  },
  actions: {
    setLogin(l:boolean) {
     this.login = l;
    }
  }
})