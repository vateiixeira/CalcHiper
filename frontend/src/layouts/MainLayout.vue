<template>
  <div class="teste">
      <h4>Orcamento Hiper</h4>
      <q-select v-model="tipo_hiper" @input="val => {calcula()}" label="Tipo do sistema" :options="opcoes_hiper" />
        <q-select v-model="caixas" @input="val => {calcula()}" label="Quantidade de caixas" :options="qtd_caixas" />
        <q-select v-model="filiais" @input="val => {calcula()}" label="Quantidade de filiais" :options="qtd_filiais" />
        <q-checkbox left-label @input="val => {calcula()}" v-model="boleto" label="Boleto ?" />
        <q-checkbox left-label @input="val => {calcula()}"  v-model="spedc" label="Sped C ?" />
        <q-checkbox left-label @input="val => {calcula()}" v-model="vendas" label="Vendas ?" />
        <q-checkbox left-label @input="val => {calcula()}" v-model="mdfe" label="MFDF-e ?" />
        <q-checkbox left-label @input="val => {calcula()}" v-model="img" label="Imagem dos produtos? (Apenas para Hiper Mini)" />
        <q-checkbox left-label @input="val => {calcula()}" v-model="connection" label="Hiper Connection" /> <br/>
        <hr>
        <span>Valor sugerido para mensalidade</span>
        <h6 >{{ valor_total }}</h6>
        <span>Custo para o Hiperador</span>
        <h6 >{{ this.total_custo }}</h6>
    </div>
</template>

<script>

export default {
  name: 'MainLayout',
  data () {
    return {
      leftDrawerOpen: false,
      opcoes_hiper: ['MINI', 'GESTAO'],
      qtd_caixas: ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
      qtd_filiais: ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
      boleto: false,
      spedc: false,
      vendas: false,
      mdfe: false,
      img: false,
      connection: false,
      valor_total: 0,
      valor_boleto: 0,
      valor_spedc: 0,
      valor_vendas: 0,
      valor_mdfe: 0,
      valor_img: 0,
      valor_connection: 0,
      valor_hiper: 0,
      valor_caixa: 0,
      valor_filiais: 0,
      tipo_hiper: null,
      caixas: null,
      filiais: null,
      total_custo: 0
    }
  },
  methods: {
    calcula () {
      if (this.boleto === true) { this.valor_boleto = 20 } else { this.valor_boleto = 0 }
      if (this.spedc === true) { this.valor_spedc = 20 } else { this.valor_spedc = 0 }
      if (this.vendas === true) { this.valor_vendas = 20 } else { this.valor_vendas = 0 }
      if (this.mdfe === true) { this.valor_mdfe = 20 } else { this.valor_mdfe = 0 }
      if (this.img === true) { this.valor_img = 20 } else { this.valor_img = 0 }
      if (this.connection === true) { this.valor_connection = 20 } else { this.valor_connection = 0 }
      if (this.tipo_hiper === 'MINI') {
        this.valor_filiais = 0; this.valor_hiper = 27; this.valor_caixa = this.caixas * 15
      } else if (this.tipo_hiper === 'GESTAO') {
        if (this.filiais > 1) {
          this.valor_filiais = this.filiais * 45 - 45
        } else {
          this.valor_filiais = 0
        } this.valor_hiper = 65; this.valor_caixa = this.caixas * 20
      } else {
        this.valor_filiais = 0; this.valor_hiper = 0; this.valor_caixa = 0
      }
      var total = this.valor_boleto + this.valor_spedc + this.valor_vendas +
                          this.valor_vendas + this.valor_mdfe + this.valor_img +
                          this.valor_connection + this.valor_hiper +
                          this.valor_caixa + this.valor_filiais
      var porcentagem = total * 0.33
      this.total_custo = total - porcentagem
      this.valor_total = this.total_custo * 3
    }
  }
}
</script>

<style>

</style>
