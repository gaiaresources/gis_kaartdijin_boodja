export type CatalogueStatus = 'locked'|'draft'|'cancelled';
export type LayerSubscriptionStatus = 'active'|'disabled';

// Raw records, currently placeholders and subject to change
export interface LayerSubscription {
  number: string
  name: string
  description: string
  subscribedDate: string
  subscribedTime: number
  webserviceUrl: string
  status: LayerSubscriptionStatus,
  refreshFrequencyMinutes: number
}

export interface CatalogueEntry {
  number: string
  name: string
  custodian: string
  status: CatalogueStatus
  lastUpdated: string
  time: string
  assignedTo: string
  description: string
}

export interface PaginationFilter extends Map<string, any> {
  offset?: number
  limit?: number
}

export interface LayerSubscriptionFilter extends PaginationFilter {
  status: LayerSubscriptionStatus
  subscribedFrom?: string
  subscribedTo?: string
}

export interface CatalogueEntryFilter extends PaginationFilter {
  custodian?: string
  status?: CatalogueStatus
  lastUpdatedFrom?: string
  lastUpdatedTo?: string
  assignedTo?: string
}

export interface PaginationState {
  currentPage: number
  numPages: number
  pageLength: number
  total: number
}
