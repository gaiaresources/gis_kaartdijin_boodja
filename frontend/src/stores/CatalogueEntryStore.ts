import { defineStore } from "pinia";
import {Ref, ref, computed, ComputedRef, watch} from 'vue';
import { BackendService } from "../backend/backend.service";
import { BackendServiceStub } from "../backend/backend.stub";
import { CatalogueEntry, CatalogueEntryFilter } from '../backend/backend.api';

// Get the backend stub if the test flag is used.
const backend: BackendService = import.meta.env.DEV ? new BackendServiceStub : new BackendService();

export const useCatalogueEntryStore = defineStore('catalogueEntries', () => {
  const catalogueEntries: Ref<Array<CatalogueEntry>> = ref([]);
  const currentPage: Ref<number> = ref(1);
  const pageSize: Ref<number> = ref(10);
  const numPages: ComputedRef<number> = computed(() => Math.ceil(catalogueEntries.value.length / pageSize.value));
  const filter: Ref<CatalogueEntryFilter> = ref(new Map() as CatalogueEntryFilter);

  watch(filter, () => getCatalogueEntries());

  async function getCatalogueEntries (): Promise<Array<CatalogueEntry>> {
    const entries = await backend.getCatalogueEntries(filter.value);
    catalogueEntries.value = entries;

    return entries;
  }

  return { catalogueEntries, currentPage, pageSize, numPages, filter, getCatalogueEntries };
});
