import {defineStore} from "pinia";
import {computed, ComputedRef, Ref, ref, watch} from "vue";
import {BackendService} from "../backend/backend.service";
import {BackendServiceStub} from "../backend/backend.stub";
import {CatalogueEntryFilter, LayerSubscription } from '../backend/backend.api';


// Get the backend stub if the test flag is used.
const backend: BackendService = import.meta.env.DEV ? new BackendServiceStub() : new BackendService();

export const useLayerSubscriptionStore = defineStore('layerSubscription', () => {
  const layerSubscriptions: Ref<Array<LayerSubscription>> = ref([]);
  const currentPage: Ref<number> = ref(1);
  const pageSize: Ref<number> = ref(10);
  const numPages: ComputedRef<number> = computed(() => Math.ceil(layerSubscriptions.value.length / pageSize.value));
  const filter: Ref<CatalogueEntryFilter> = ref(new Map() as CatalogueEntryFilter);

  watch(filter, () => getLayerSubscriptions());

  async function getLayerSubscriptions(): Promise<Array<LayerSubscription>> {
    const subscriptions = await backend.getLayerSubscriptions(filter.value);
    layerSubscriptions.value = subscriptions;

    return subscriptions;
  }

  return { layerSubscriptions, currentPage, pageSize, numPages, filter, getLayerSubscriptions };
});
