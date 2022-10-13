// Raw records, currently placeholders and subject to change
export interface LayerSubscription {
  number: string
  name: string
  description: string
  subscribedDate: string
  subscribedTime: number
  webserviceUrl: string
  status: 'active'|'disabled',
  refreshFrequencyMinutes: number
}

export interface CatalogueEntry {
  number: string
  name: string
  custodian: string
  status: 'locked'|'draft'|'cancelled'
  lastUpdated: string
  time: string
  assignedTo: string
  description: string
}
