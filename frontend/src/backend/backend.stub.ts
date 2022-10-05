import { BackendService } from "./backend.service";
import { LayerSubscription } from "./backend.api";

const DUMMY_LAYER_SUBSCRIPTIONS: Array<LayerSubscription> = [
  {
    id: 'LS0000001',
    name: 'Hotspots (Firewatch)',
    description: '',
    subscribedDate: '10/02/2022',
    subscribedTime: 1000,
    webserviceUrl: 'https://services.slip.wa.gov.au/',
    status: 'active'
  }
];

export class BackendServiceStub implements BackendService {
  public getLayerSubscriptions (): Array<LayerSubscription> {
    return DUMMY_LAYER_SUBSCRIPTIONS;
  }
}
