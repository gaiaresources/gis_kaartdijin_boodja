<script setup lang="ts">
  import LayerSubscriptionDataTable from './dataTable/LayerSubscriptionDataTable.vue';
  import { ref, onMounted } from 'vue';
  import { useCatalogueEntryStore } from '../stores/CatalogueEntryStore';
  import { useLayerSubscriptionStore } from '../stores/LayerSubscriptionStore';
  import CatalogueEntryDataTable from './dataTable/CatalogueEntryDataTable.vue';
  import { storeToRefs } from 'pinia';
  import type { Ref } from 'vue';

  type SelectedTab = 'catalogueEntries'|'layerSubmissions'|'layerSubscriptions';

  const selectedTab: Ref<SelectedTab> = ref('catalogueEntries');

  function setSelectedTab (tab: SelectedTab) {
    selectedTab.value = tab;
  }

  // get Stores and fetch with `storeToRef` to
  const catalogueEntryStore = useCatalogueEntryStore();
  const { catalogueEntries } = storeToRefs(catalogueEntryStore);
  const { getCatalogueEntries } = catalogueEntryStore;

  const layerSubscriptionStore = useLayerSubscriptionStore();
  const { layerSubscriptions } = storeToRefs(layerSubscriptionStore);
  const { getLayerSubscriptions } = layerSubscriptionStore;

  onMounted(() => {
    getCatalogueEntries();
    getLayerSubscriptions();
  });
</script>

<template>
  <ul class="nav nav-pills mb-4">
    <li class="nav-item">
      <button class="nav-link" aria-current="page" href="#" :class='{ active: selectedTab === "catalogueEntries" }'
              @click='setSelectedTab("catalogueEntries")'>Catalogue Entries</button>
    </li>
    <li class="nav-item">
      <button class="nav-link" href="#" :class='{ active: selectedTab === "layerSubmissions" }'
              @click='setSelectedTab("layerSubmissions")'>Layer Submissions</button>
    </li>
    <li class="nav-item">
      <button class="nav-link" href="#" :class='{ active: selectedTab === "layerSubscriptions" }'
              @click='setSelectedTab("layerSubscriptions")'>Layer Subscriptions</button>
    </li>
  </ul>
  <div class="card">
    <div class="card-header">
      <h4>Layer Subscriptions</h4>
    </div>
    <div class="card-body">
      <div id="layerSubscriptionAccordion" class="accordion">
        <div class="accordion-item">
          <h2 id="headingFilter" class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFilters" aria-expanded="true" aria-controls="collapseFilters">
              Filters
            </button>
          </h2>
          <div id="collapseFilters" class="accordion-collapse collapse show" aria-labelledby="headingFilter" data-bs-parent="#layerSubscriptionAccordion">
            <div class="accordion-body">
              <form class="form d-flex gap-3">
                <div class="form-floating">
                  <select id="statusSelect" class="form-select form-select-sm w-auto" aria-label="Status select">
                    <option selected>Open this select menu</option>
                    <option value="1">One</option>
                    <option value="2">Two</option>
                    <option value="3">Three</option>
                  </select>
                  <label for="statusSelect">Status</label>
                </div>
                <div class="form-floating">
                  <input id="subscribedFromInput" type="date" class="form-control w-auto" placeholder="DD/MM/YYYY">
                  <label for="statusSelect">Subscribed from</label>
                </div>
                <div class="form-floating">
                  <input id="subscribedToInput" type="date" class="form-control w-auto" placeholder="DD/MM/YYYY">
                  <label for="statusSelect">Subscribed to</label>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <catalogue-entry-data-table v-if='selectedTab === "catalogueEntries"' :rows="catalogueEntries"/>
      <layer-subscription-data-table v-if='selectedTab === "layerSubscriptions"' :rows="layerSubscriptions"/>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  #layerSubscriptionAccordion {
    .accordion-item {
      .accordion-body .form-floating {
        select, input {
          min-width: 15rem;
        }
      }
    }
  }
</style>
