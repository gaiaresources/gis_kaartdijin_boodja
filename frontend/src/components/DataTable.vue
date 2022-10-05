<script lang="ts" setup>
  import MinusCircleFill from "./icons/minusCircleFill.vue";
  import PlusCircleFill from "./icons/plusCircleFill.vue";
  import { useLayerSubscriptionStore } from "../stores/LayerSubscriptionStore.js";

  const layerSubscriptionStore = useLayerSubscriptionStore();

  layerSubscriptionStore.getLayerSubscriptions();
</script>

<template>
  <table class="table table-bordered table-striped table-hover mb-1">
    <thead>
      <tr>
        <th>Number</th>
        <th>Name</th>
        <th>Subscribed date</th>
        <th>Time</th>
        <th>Webservice URL</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="layerSubscription in layerSubscriptionStore.layerSubscriptions" :key="layerSubscription.id">
        <td>
          <MinusCircleFill colour="#D33333" class="me-2"/>
          {{ layerSubscription.id }}
        </td>
        <td>{{ layerSubscription.name }}</td>
        <td>{{ layerSubscription.subscribedDate }}</td>
        <td>{{ layerSubscription.subscribedTime }}</td>
        <td>{{ layerSubscription.webserviceUrl }}</td>
        <td>{{ layerSubscription.status }}</td>
        <td><a href="#">View</a></td>
      </tr>
      <tr>
        <td colspan="7"><PlusCircleFill colour="#4284BC"></PlusCircleFill></td>
      </tr>
    </tbody>
  </table>
  <span class="ms-2 small fw-bold">Showing 1 to x of y entries</span>
  <nav aria-label="Table navigation" class="d-flex justify-content-end">
    <ul class="pagination">
      <li class="page-item"><a class="page-link" href="#">Previous</a></li>
      <li class="page-item"><a class="page-link" href="#">1</a></li>
      <li class="page-item"><a class="page-link" href="#">Next</a></li>
    </ul>
  </nav>
</template>
