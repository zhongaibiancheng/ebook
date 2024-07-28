import { createRouter, createWebHistory } from "vue-router";
import Index from "../views/Index.vue";
import Price from "../views/Price.vue";
import Payment from "../views/Payment.vue";
import BuyDirectly from "../views/BuyDirectly.vue"
import CreateBook from "../views/CreateBook.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "index",
      component: Index
    },
    {
      path: "/price",
      name: "price",
      component: Price
    },
    {
      path: "/payment",
      name: "payment",
      component: Payment
    },
    {
      path:"/buy_directly",
      name:"buy_directly",
      component:BuyDirectly
    },
    {
      path: "/create_book",
      name: "create_book",
      component:CreateBook
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import("../views/AboutView.vue")
    }
  ]
});

export default router;
