import { defineStore } from "pinia";
import { Ref, ref } from "vue";
import { BackendService } from "../backend/backend.service";
import { BackendServiceStub } from "../backend/backend.stub";
import { CatalogueEntry } from '../backend/backend.api';

export interface TableData {
  headers: Array<string>
  rows: Array<string>
}

// Get the backend stub if the test flag is used.
const backend: BackendService = import.meta.env.DEV ? new BackendServiceStub : new BackendService();

export const useCatalogueEntryStore = defineStore('catalogueEntries', () => {
  const catalogueEntries: Ref<Array<CatalogueEntry>> = ref([]);

  function getCatalogueEntries (): Array<CatalogueEntry> {
    const entries = backend.getCatalogueEntries();
    catalogueEntries.value = entries;

    return entries;
  }

  return { catalogueEntries, getCatalogueEntries };
});
