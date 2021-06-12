import {Asset} from './org.hyperledger.composer.system';
import {Participant} from './org.hyperledger.composer.system';
import {Transaction} from './org.hyperledger.composer.system';
import {Event} from './org.hyperledger.composer.system';
// export namespace org.example.smsc{
   export class Spammer extends Asset {
      phoneNumber: string;
      description: string;
      owner: Admin;
   }
   export class Classifier extends Asset {
      phoneNumber: string;
      description: string;
      owner: Admin;
   }
   export class Admin extends Participant {
      id: string;
      name: string;
      email: string;
   }
   export class Validate extends Transaction {
      spammer: Spammer;
      newOwner: Admin;
   }
   export class ValidateNotification extends Event {
      spammer: Spammer;
   }
   export class RemoveNotification extends Event {
      spammer: Spammer;
   }
// }
