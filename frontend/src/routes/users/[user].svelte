<!-- frontend/src/routes/users/[user].svelte -->
<script context="module">
   export async function preload({ params, query }) {
      const res = await this.fetch(`http://localhost:3737/contracts/apd_v01/State?key=${params.user}`) // this should be the masternode
      const data = await res.json();
      if (data.value === 'undefined') this.error(res.status, data.message);
      if (data.value === null) data.value = 0;
      return { value: data.value, user: params.user };
   }

// probably walletController in the header
</script>

<script>
    import { goto } from '@sapper/app';

    export let user;
    export let value;

   let receiver = "";
   let amount = 0;

   const transfer = async () => {
      const transaction = {
         sender: user,
         contract: 'apd_v01',
         method: 'transfer',
         args: {
            receiver,
            amount
         }
      }

   const refreshBalance = async () => {
      const res = await fetch("http://localhost:3737/contracts/apd_v01/State?key=" + user)
      let data = await res.json();
      value = data.value;
      }

   const clearInputs = () => {
      receiver = ""
      amount = 0
   }

   const logout = () => {
      goto(`.`);
   }

      const options = {
         method: 'POST',
         headers: {
            'Content-Type': 'application/json'
         },
         body: JSON.stringify(transaction)
      }

      const res = await fetch(`http://localhost:3737/`, options)
      const data = await res.json();
      if (data.error) {
         alert(data.error);
      } else {
         alert("You sent " + amount + " token(s) to " + receiver + "!");
         clearInputs();
         refreshBalance();
            }
   }
</script>

<style>
   p { font-size: 1.2em; }
   .shadowbox { padding: 0.5rem 20px; }
   form{
      padding: 50px;
      color: #461BC2;
      display:flex;
      flex-direction: column;
      border: none;
      box-sizing: border-box;
   }
   form > h2{
      margin: 0;
      font-weight: 600;
      line-height: 2.2;
      letter-spacing: 1px;
   }
   form > input{
      margin-bottom: 1rem;
   }
   input[type="submit"] {
      margin-right: 20px;
   }
   .buttons {
      display: flex;
      flex-direction: row;
      justify-content: flex-end;
      margin-top: 1rem;
   }
</style>

<svelte:head>
   <title>{user + "'s Tokens"}</title>
</svelte:head>

<h1>{"Hello " + user + "!"}</h1>
<h2>Token Balance: {value}</h2>

<form on:submit|preventDefault={transfer}>
   <h3>Make a transfer</h3>
   <label for="to">To</label>
   <input type="text" name="to" bind:value={receiver} required="true"/>
   <label for="amount">Token Amount</label>
   <input type="number" name="amount" bind:value={amount} required="true"/>
   <div class="buttons">
        <input class="button" type="submit" value="send"/>
        <button class="button" on:click={logout}>sign out </button>
   </div>
</form>
