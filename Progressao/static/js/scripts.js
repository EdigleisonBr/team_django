var baseUrl = 'http://localhost:8000/cadastrar/gol/';
var ids = [];
var nomes = [];
var gols = [];

$(document).ready(function(){
    // Se não houver Time não pode inserir Gols.
    if ($("#id_time").val() == ''){
        $("#id_gols_contra" ).prop("disabled", true );
    }

    var btnCadastrar = $('.btn-cadastrar');
    var btnSalvar = $('#salvar-gols');
    var salvarForm = $('#salvar-form');
    var deleteBtn  = $('.btn-deletar');
    var deleteBtnGols  = $('.btn-deletar-gols');
    var time  = $('#id_time');

    // Impede o usuário de mandar dados sem preencher ou repetir o atleta na listagem e monta o HTML da tabela. (INUTILIZADO)
    $(btnCadastrar).on('click', function(e) {
        var atleta_existe = false;
        var nome_vazio = false;
        var gols_vazio = false;
        var index = 0;
        var coleta = document.getElementById("nome").value;
        var coleta_gols = document.getElementById("gols").value;
        var nome = coleta.split('-');

        if (coleta == 0){
            nome_vazio = true;
        }
        if ((coleta_gols == '') || (coleta_gols == 0)){
            gols_vazio = true;
        }

        len_id = ids.length;
                
        if (len_id > 0){
            for (let i=0 ; i < len_id ; i++){
                if (ids[i] == nome[0]){
                    atleta_existe = true;
                }    
            }
        }
             
        if ((coleta == 0) || (coleta_gols == '') || (coleta_gols == 0) || (atleta_existe)) {
            if (atleta_existe){
                msg = 'Este atleta já foi cadastrado, exclua e insira os dados novamente!'
            }
            if (nome_vazio == true){
                msg = 'Preencha o nome do atleta!'
            }
            if (gols_vazio == true){
                msg = 'Preencha a quantidade de gols!!'
            }
            if ((nome_vazio == true) && (gols_vazio == true)){
                msg = 'Preencha o nome do atleta e a quantidade de gols!'
            }
            Swal.fire({
                title: 'Atenção!',
                text: msg,
                icon: 'warning',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'OK'
            }).then((result) => {
                if (result.isConfirmed) {
                    if ((nome_vazio == true) && (gols_vazio == true)){
                        $("#nome").focus();
                    };
                    if (nome_vazio == true){
                        $("#nome").focus();
                    };
                    if (gols_vazio == true){
                        $("#gols").focus();
                    };
                };
            });
        }
        else {
            //Adiciona os valores no HTML
            $('#lista').append(
                '<tr id="date' + index + '">' +
                '   <td class="d-none">' + (parseInt(index)+1) + '</td>' +
                '   <td>' + nome[1] + '</td>' +
                '   <td>' + coleta_gols + '</td>' +
                '   <td class="text-center">' +
                '       <i onclick="removeAtleta(\'' + index + '\')" class="fas fa-times text-danger"></i>' +
                '   </td>' +
                '</tr>'
            );
            //função para adicionar mais um nome à lista
            var coleta = document.getElementById("nome").value;
            var coleta_gols = document.getElementById("gols").value;

            ids.push(nome[0]);
            nomes.push(nome[1]);
            gols.push(coleta_gols);
                   
            document.getElementById('jogoId').value = nome[2];
            document.getElementById('arrayId').value = ids;
            document.getElementById('arrayA').value = nomes;
            document.getElementById('arrayG').value = gols;

            //Limpar dados dos campos
            $("#nome").val(0);
            $("#gols").val("");
        }
    });   

    // Impede o usuário de Salvar os gols antes e adicionar os dados
    $(btnSalvar).on('click', function(e) {
        if ((document.getElementById('arrayId').value == '') &&(document.getElementById('gols_contra').value == '')){
            Swal.fire({
                title: 'Atenção!',
                text: 'Insira os dados antes de salvar!',
                icon: 'error',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'OK'
            })
        }
        else{
        salvarForm.submit();
        }
    });

    // Gera mensagem para o usuário antes de deletar qualquer cadastro.
    $(deleteBtn).on('click', function(e) {
        var delLink = $(this).attr('href');
        
        e.preventDefault(); // Cancela a ação do <a> para não deletar a Tarefa já "de cara".
        
        var delLink = $(this).attr('href');
                        
        Swal.fire({
            title: 'Atenção!',
            text: "Deseja mesmo excluir esse cadastro?",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sim'
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = delLink;
            }
        });
    });

    // Gera mensagem para o usuário no momento em que ele estiver exluindo os Gols.
    $(deleteBtnGols).on('click', function(e) {
        var delLink = $(this).attr('href');

        e.preventDefault(); // Cancela a ação do <a> para não deletar a Tarefa já "de cara".
        
        var delLink = $(this).attr('href');
                        
        Swal.fire({
            title: 'Atenção!',
            text: "Esta ação excluirá todos os gols?",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sim'
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = delLink;
            }
        });
    });

    // Se não houver time não pode haver Gols Contra
    $(time).on('click', function(e) {
        let gols_contra = $("#id_gols_contra").val();
        let time = $("#id_time").val();
        console.log("gols_contra: ",gols_contra);
        console.log('time: ', time);

        if (time == ''){
            $("#id_gols_contra" ).prop("disabled", true );
            $("#id_gols_contra" ).val("");
        }
        else{
            $("#id_gols_contra" ).prop("disabled", false);
        }
    });
    
});

// Remove atleta da listagem de gols (INUTILIZADO)
function removeAtleta (index) {
    $('#date' + index).remove();
            
    nomes.splice(index, 1);
    gols.splice(index, 1);

    document.getElementById('arrayA').value = nomes;
    document.getElementById('arrayG').value = gols; 
}