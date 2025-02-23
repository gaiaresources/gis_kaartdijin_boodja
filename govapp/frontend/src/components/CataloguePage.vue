<script setup lang="ts">
  import { computed, ComputedRef, ref, watch } from "vue";
  import LayerSubscriptionDataTable from "./dataTable/LayerSubscriptionDataTable.vue";
  import CatalogueEntryDataTable from "./dataTable/CatalogueEntryDataTable.vue";
  import CatalogueEntryFilter from "./widgets/CatalogueEntryFilter.vue";
  import LayerSubscriptionFilter from "./widgets/LayerSubscriptionFilter.vue";
  import LayerSubmissionDataTable from "./dataTable/LayerSubmissionDataTable.vue";
  import LayerSubmissionFilter from "./widgets/LayerSubmissionFilter.vue";
  import CatalogueEntryDetailView from "./detailViews/EntryDetailView.vue";
  import CommunicationsLogModal from "../components/modals/CommunicationsLogModal.vue";
  import { CatalogueDetailViewTabs, CatalogueTab, CatalogueView, NavigateEmitsOptions, SubmissionDetailViewTabs,
    SubscriptionDetailViewTabs } from "./viewState.api";
  import Card from "./widgets/Card.vue";
  import Accordion from "./widgets/Accordion.vue";
  import SideBarLeft from "./SideBarLeft.vue";
  import { CatalogueEntry } from "../providers/catalogueEntryProvider.api";
  import { LayerSubscription } from "../providers/layerSubscriptionProvider.api";
  import { LayerSubmission } from "../providers/layerSubmissionProvider.api";
  import { catalogueEntryProvider } from "../providers/catalogueEntryProvider";
  import { layerSubmissionProvider } from "../providers/layerSubmissionProvider";
  import { layerSubscriptionProvider } from "../providers/layerSubscriptionProvider";
  import { useCatalogueEntryStore } from "../stores/CatalogueEntryStore";
  import { useLayerSubmissionStore } from "../stores/LayerSubmissionStore";
  import { useLayerSubscriptionStore } from "../stores/LayerSubscriptionStore";
  import { storeToRefs } from "pinia";
  import { ModalTypes } from "../stores/ModalStore.api.js";
  import { useModalStore } from "../stores/ModalStore";
  import SubmissionDetailView from "./detailViews/SubmissionDetailView.vue";
  import SubscriptionDetailView from "./detailViews/SubscriptionDetailView.vue";
  import { usePermissionsComposable } from "../tools/permissionsComposable";
  import AttributesModal from "./modals/AttributesModal.vue";
  import NotificationsModal from "./modals/NotificationsModal.vue";

  const { catalogueEntries } = storeToRefs(useCatalogueEntryStore())
  const modalStore = useModalStore();

  const selectedTab = ref<CatalogueTab>(CatalogueTab.CatalogueEntries);
  const selectedView = ref<CatalogueView>(CatalogueView.List);
  const selectedEntryDetailTab = ref<CatalogueDetailViewTabs>(CatalogueDetailViewTabs.Details)
  const selectedSubmissionDetailTab = ref<SubmissionDetailViewTabs>(SubmissionDetailViewTabs.Details)
  const selectedSubscriptionDetailTab = ref<SubscriptionDetailViewTabs>(SubscriptionDetailViewTabs.Details)
  const selectedViewEntry = ref<CatalogueEntry | undefined>();
  const selectedViewSubmission = ref<LayerSubmission | undefined>();
  const selectedViewSubscription = ref<LayerSubscription | undefined>();
  const showAttributeModal: ComputedRef<boolean> = computed(
    () => [ModalTypes.AttributeEdit, ModalTypes.AttributeAdd, ModalTypes.AttributeDelete]
      .includes(modalStore.activeModal));
  const showNotificationModal: ComputedRef<boolean> = computed(() => [ModalTypes.NotificationEdit,
    ModalTypes.NotificationAdd, ModalTypes.NotificationDelete]
    .includes(modalStore.activeModal));

  const permissionsComposable = usePermissionsComposable(selectedViewEntry.value);
  const currentEntryView = computed(() => {
    return permissionsComposable.isLoggedInUserAdmin.value || permissionsComposable.isLoggedInUserEditor.value ?
      CatalogueView.Edit :
      CatalogueView.View;
  })

  watch(catalogueEntries, () => {
    selectedViewEntry.value = catalogueEntries.value?.find((entry: CatalogueEntry) => entry.id === selectedViewEntry.value?.id);
    permissionsComposable.updateCurrentEntry(selectedViewEntry.value);
  }, { deep: true });

  async function navigate (tab: CatalogueTab, view: CatalogueView, options?: NavigateEmitsOptions) {
    selectedView.value = view;
    selectedViewEntry.value = undefined;
    selectedViewSubmission.value = undefined;
    selectedViewSubscription.value = undefined;

    selectedTab.value = tab;
    selectedView.value = view;

    if (typeof options?.recordId !== "number") {
      return;
    } else if (tab === CatalogueTab.CatalogueEntries) {
      selectedViewEntry.value = await catalogueEntryProvider.fetchCatalogueEntry(options.recordId);
      if (options?.viewTab) {
        selectedEntryDetailTab.value = options.viewTab as CatalogueDetailViewTabs;
      }
    } else if (tab === CatalogueTab.LayerSubscriptions) {
      selectedViewSubscription.value = await layerSubscriptionProvider.fetchLayerSubscription(options.recordId);
      if (options?.viewTab) {
        selectedSubscriptionDetailTab.value = options.viewTab as SubscriptionDetailViewTabs;
      }
    } else if (tab === CatalogueTab.LayerSubmissions) {
      selectedViewSubmission.value = await layerSubmissionProvider.fetchLayerSubmission(options.recordId);
      if (options?.viewTab) {
        selectedSubmissionDetailTab.value = options.viewTab as SubmissionDetailViewTabs;
      }
    } else {
      console.warn("Selected view record was not a recognised type");
    }
  }

  const { clearFilters: clearEntryFilters } = useCatalogueEntryStore();
  const { clearFilters: clearSubmissionFilters } = useLayerSubmissionStore();
  const { clearFilters: clearSubscriptionFilters } = useLayerSubscriptionStore();

  function onClearClick() {
    clearEntryFilters();
    clearSubmissionFilters();
    clearSubscriptionFilters();
  }
</script>

<template>
  <ul class="nav nav-pills mb-4" v-if="selectedView === CatalogueView.List">
    <li class="nav-item">
      <button class="nav-link" aria-current="page" href="#"
              :class='{ active: selectedTab === CatalogueTab.CatalogueEntries }'
              @click='navigate(CatalogueTab.CatalogueEntries, CatalogueView.List)'>Catalogue Entries</button>
    </li>
    <li class="nav-item">
      <button class="nav-link" href="#"
              :class='{ active: selectedTab === CatalogueTab.LayerSubmissions }'
              @click='navigate(CatalogueTab.LayerSubmissions, CatalogueView.List)'>Layer Submissions</button>
    </li>
    <li class="nav-item">
      <button class="nav-link" href="#" :class='{ active: selectedTab === CatalogueTab.LayerSubscriptions }'
              @click='navigate(CatalogueTab.LayerSubscriptions, CatalogueView.List)'>Layer Subscriptions</button>
    </li>
  </ul>

  <div class="d-flex flex-row">
    <div id="side-bar-wrapper" v-if="selectedView === CatalogueView.View">
      <side-bar-left :entry="selectedViewEntry"/>
    </div>
    <div class="w-100">
      <card v-if="selectedView === CatalogueView.List">
        <template #header>
          <h4>{{ selectedTab }}</h4>
        </template>
        <template #body>
          <accordion id="filter-accordion" id-prefix="filter" header-text="Filters" class="mb-2">
            <template #body>
              <form class="form d-flex gap-3">
                <catalogue-entry-filter v-if="selectedTab === CatalogueTab.CatalogueEntries"/>
                <layer-submission-filter  v-if="selectedTab === CatalogueTab.LayerSubmissions"/>
                <layer-subscription-filter v-if="selectedTab === CatalogueTab.LayerSubscriptions"/>
              </form>
              <div class="d-flex">
                <button class="btn btn-sm btn-link link-info align-self-end ms-auto pt-0 mb-1" @click="onClearClick">
                  <small>Clear Filters</small>
                </button>
              </div>
            </template>
          </accordion>
          <catalogue-entry-data-table v-if='selectedTab === CatalogueTab.CatalogueEntries' :view="currentEntryView"
            @navigate="navigate"/>
          <layer-submission-data-table v-if='selectedTab === CatalogueTab.LayerSubmissions' @navigate="navigate"/>
          <layer-subscription-data-table v-if='selectedTab === CatalogueTab.LayerSubscriptions' @navigate="navigate"/>
        </template>
      </card>
      <catalogue-entry-detail-view
        v-if="selectedTab === CatalogueTab.CatalogueEntries && selectedView === CatalogueView.View || CatalogueView.Edit &&
        !!selectedViewEntry" :catalogue-entry="selectedViewEntry"
        :active-tab="selectedEntryDetailTab" @navigate="navigate"/>
      <submission-detail-view
        v-if="selectedTab === CatalogueTab.LayerSubmissions && selectedView === CatalogueView.View &&
         !!selectedViewSubmission" :layer-submission="selectedViewSubmission"
        :active-tab="selectedSubmissionDetailTab" @navigate="navigate"/>
      <subscription-detail-view
        v-if="selectedTab === CatalogueTab.LayerSubscriptions && selectedView === CatalogueView.View &&
         !!selectedViewSubscription" :layer-subscription="selectedViewSubscription"
        :active-tab="selectedSubscriptionDetailTab" @navigate="navigate"/>
    </div>
  </div>
  <communications-log-modal v-if="selectedViewEntry" :catalogue-entry="selectedViewEntry"
    :show="modalStore.activeModal === ModalTypes.CommsLog || modalStore.activeModal === ModalTypes.CommsLogAdd"
    :add-log="modalStore.activeModal === ModalTypes.CommsLogAdd"/>
  <attributes-modal v-if="selectedViewEntry" :catalogue-entry="selectedViewEntry"
                    :show="showAttributeModal" :mode="showAttributeModal ? modalStore.activeModal : ModalTypes.None"/>
  <notifications-modal v-if="selectedViewEntry" :catalogue-entry="selectedViewEntry" :show="showNotificationModal"
                       :mode="showNotificationModal ? modalStore.activeModal : ModalTypes.None"/>
</template>

<style lang="scss">
  #filter-accordion {
    .accordion-collapse .accordion-body {
      form {
        overflow-x: auto;
      }
      padding-bottom: 0;
    }
  }

  #side-bar-wrapper {
    width: 24rem;
  }
</style>
