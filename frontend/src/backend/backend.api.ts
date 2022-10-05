// Raw records, currently placeholders and subject to change
export interface LayerSubscription {
  id: string
  name: string
  description: string
  subscribedDate: string
  subscribedTime: number
  webserviceUrl: string
  status: 'active'|'disabled'
}
