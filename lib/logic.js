/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

'use strict';
/**
 * Write your transction processor functions here
 */

/**
 * @param {org.example.smsc.Validate} validate - Validating filtering
 * @transaction
 */
 async function validateSpammer(validate) {
    validate.spammer.owner = validate.newOwner;
  const assetRegistry = await getAssetRegistry('org.example.smsc.Spammer');
  
    // emit a notification that a trade has occurred
 //   const validateNotification = getFactory().newEvent('org.example.smsc', 'ValidateNotification');
  //  validateNotification.spammer = validate.spammer;
  //  emit(validateNotification);

    // persist the state of the commodity
    await assetRegistry.update(validate.spammer);
}