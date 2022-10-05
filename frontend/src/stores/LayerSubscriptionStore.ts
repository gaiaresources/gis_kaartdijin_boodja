import {defineStore} from "pinia";
import {Ref, ref} from "vue";
import {BackendService} from "../backend/backend.service";
import {BackendServiceStub} from "../backend/backend.stub";
import {LayerSubscription} from "../backend/backend.api";


export const useLayerSubscriptionStore = defineStore('layerSubscription', () => {
  // Get the backend stub if the test flag is used.
  const backend: BackendService = import.meta.env.DEV ? new BackendServiceStub : new BackendService();
  const layerSubscriptions: Ref<Array<LayerSubscription>> = ref([]);

  function getLayerSubscriptions (): Array<LayerSubscription> {
    const subscriptions = backend.getLayerSubscriptions();
    layerSubscriptions.value = subscriptions;
    return subscriptions;
  }

  return { layerSubscriptions, getLayerSubscriptions };
})
