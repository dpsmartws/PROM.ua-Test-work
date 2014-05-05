

function init(){
	// Привязываем события к элементам начальной формы
	try {  
		var nickname = document.getElementById('nickname');
		var password = document.getElementById('password');
		var registration_button = document.getElementById('registration_button');
		nickname.onclick = function() {
									if (this.value == "Имя пользователя"){
										this.value = "";
										}
									};
									
		nickname.onblur = function() {
									if (this.value == ""){
										this.value = "Имя пользователя";
										}
									};
									
									
		password.onclick = function() {
									if (this.value == "Пароль"){
										this.value = "";
										this.type = "password";
										}
									};
		password.onblur = function() {
									if (this.value == ""){
										this.value = "Пароль";
										this.type = "text";
										}
									};
		registration_button.onclick = function() {
									create_registration_form();
									};
	}  catch(e){
	}
	
	// Привязываем события к кнопке панели управления
	try{
		
		var panel_button = document.getElementById('control_panel_button');
		panel_button.onclick = function(){
							
							var control_form = document.getElementById('control_form');
							if (!control_form){
									this.innerHTML = "<span>Скрыть панель управления</span>";
									load_control_form();
								}
							else{
									var content = document.getElementById('content');
									content.removeChild(control_form);
									this.innerHTML = "<span>Открыть панель управления</span>";
								}
							}
	} catch(e){
	}
	
	// Привязываем события к элементам формы регистрации
	try {
		var nickname2 = document.getElementById('nickname2');
		nickname2.onclick = function() {
									if (this.value == "Имя пользователя"){
										this.value = "";
										}
									};
									
		nickname2.onblur = function() {
									if (this.value == ""){
										this.value = "Имя пользователя";
										}
									};
									
		var password1 = document.getElementById('password1');
		password1.onclick = function() {
									if (this.value == "Пароль"){
										this.value = "";
										this.type = "password";
										}
									};
		password1.onblur = function() {
									if (this.value == ""){
										this.value = "Пароль";
										this.type = "text";
										}
									};
									
		var password2 = document.getElementById('password2');
		password2.onclick = function() {
									if (this.value == "Подтверждение"){
										this.value = "";
										this.type = "password";
										}
									};
		password2.onblur = function() {
									if (this.value == ""){
										this.value = "Подтверждение";
										this.type = "text";
										}
									};
		var email2 = document.getElementById('email2');
		email2.onclick = function() {
									if (this.value == "Эмеил"){
										this.value = "";
										}
									};
		email2.onblur = function() {
									if (this.value == ""){
										this.value = "Эмеил";
										}
									};
	} catch(e){
	}
	
	// Привязываем события к блоку поиска
	try {
		var search_line = document.getElementById('search_line');
		search_line.onclick = function(){
								
									if (this.value == "Начните вводить название книги:)"){
										this.value = "";
										}
									};
		search_line.onkeyup = function(){
										send_search_data(this.value);
									};
		document.body.onclick = function(){
								try{
									var search_block = document.getElementById('searchblock');
									var result_block = document.getElementById('result_block');
									search_block.removeChild(result_block);
								} catch(e){
								}
						};
						
	} catch(e){
	}
	
	
	}
	
	
function load_control_form(){
		data = {load:"books"};
		$.ajax({
			url:"/library/load",
			type:"POST",
			data:data,
			dataType:"json",
			success:show_control_form,
			error:clear_block('books_block')
				});
		data = {load:"authors"};
		$.ajax({
			url:"/library/load",
			type:"POST",
			data:data,
			dataType:"json",
			success:show_control_form,
			error:clear_block('authors_block')
				});
	}

function clear_block(block_name){
	var block = document.getElementById(block_name);
			if (block){
			 block.innerHTML = '';
			}
	}
function show_control_form(data){
	var control_form = document.getElementById('control_form');
	if (!control_form){
		  control_form = document.createElement('div');
		  control_form.id = "control_form";
		  var content = document.getElementById('content');
		  content.appendChild(control_form);
		}
	console.log(data);
	if (data[0]['class_name'] == "Author"){
			var authors_block = document.getElementById('authors_block');
			if (!authors_block){
			  authors_block = document.createElement('div');
			  authors_block.id = "authors_block";
			}
			authors_block.innerHTML = '';
			control_form.appendChild(authors_block);
			$("#authors_block").append('<h3>Список авторов</h3>');
			$("#authors_block").append('<table id="authors_table">');
			$("#authors_table").append('<tr><td colspan=2 style="border-top:none;"><p>Добавить автора</p><div class="buttons"><a><img src="/static/images/plus.png" title="Добавить автора" onclick="load_edit_form(0, \'author\');"/></a></div></td></tr>');
			for (i=0;object = data[i];i++){
				$("#authors_table").append('<tr><td class="left"><p>'+object['id']+'</p></td><td><p>'+object['fields']['name']+' '+object['fields']['second_name']+' '+object['fields']['last_name']+'</p><div class="buttons"><a><img src="/static/images/pen.png" title="Редактировать автора" onclick="load_edit_form('+object['id']+', \'author\');"/></a><a href="/author/'+object['id']+'"><img src="/static/images/eye.png" title="Смотреть"/></a><a onclick="delete_object(\''+object['id']+'\', \'author\');"><img src="/static/images/close.png" title="Удалить книгу"/></a></div></td></tr>')
				}
			//$("#authors_block").append('</table>');
		}
	if (data[0]['class_name'] == "Book"){
			var books_block = document.getElementById('books_block');
			if (!books_block){
			  books_block = document.createElement('div');
			  books_block.id = "books_block";
			}
			books_block.innerHTML = '';
			control_form.appendChild(books_block);
			$("#books_block").append('<h3>Список книг</h3>');
			$("#books_block").append('<table id="books_table">');
			$("#books_table").append('<tr><td colspan=2 style="border-top:none;"><p>Добавить книгу</p><div class="buttons"><a><img src="/static/images/plus.png" title="Добавить книгу" onclick="load_edit_form(0, \'book\');"/></a></div></td></tr>');
			for (i=0;object = data[i];i++){
				
				$("#books_table").append('<tr><td class="left"><p>'+object['id']+'</p></td><td><p>'+object['fields']['name']+'</p><div class="buttons"><a ><img src="/static/images/pen.png" title="Редактировать книгу" onclick="load_edit_form('+object['id']+', \'book\');"/></a><a href="/book/'+object['id']+'"><img src="/static/images/eye.png" title="Смотреть"/></a><a  onclick="delete_object(\''+object['id']+'\', \'book\');"><img src="/static/images/close.png" title="Удалить книгу"/></a></div></td></tr>')
				}
			//$("#books_block").append('</table>');
		}
	
	}

function send_search_data(string){
		data = {search_string:string};
		$.ajax({
			type:"POST",
			url:"/library/search",
			data:data,
			dataType:"json",
			success:show_search_result
				});
		
	}

function show_search_result(data){
	var result_block = document.getElementById('result_block');
	if (!result_block){
		var result_block = document.createElement('div');
		result_block.id = "result_block";
	}
	result_block.innerHTML = '';
	var search_block = document.getElementById('searchblock');
	for (i=0;object = data[i];i++){
		console.log(object);
		if (object['class_name'] == "Book"){
			$('#result_block').append('<a href="/book/'+object['id']+'"><p>'+object['fields']['name']+'</p></a>');
			}
		else{
			$('#result_block').append('<a href="/author/'+object['id']+'"><p>'+object['fields']['name']+' '+object['fields']['second_name']+' '+object['fields']['last_name']+'</p></a>');
			}
		}
	search_block.appendChild(result_block);
	}
	
function create_registration_form(){
	var background = document.createElement('div');
		background.id = "additional_background";
		background.onclick = function(){
			try	{
				var form_block = document.getElementById('additional_form_block')
				document.body.removeChild(form_block);
				document.body.removeChild(this);
			} catch(e){
			}
			}
	var form_block = document.createElement('div');
	form_block.id = "additional_form_block";
	var form = document.createElement('div');
	form.id = "additional_form";
	form.innerHTML = "\
						<p>Введите данные для регистрации:)</p>\
						<form action='/registration/' method='POST' name='additional_form'>\
							"+reg_token+"\
							<input id='nickname2' name='nickname' type='text' value='Имя пользователя'>\
							<input id='password1' name='password' type='text' value='Пароль'>\
							<input id='password2' name='password2' type='text' value='Подтверждение'>\
							<input name='button' type='submit' id='button' value='ЗАРЕГИСТРИРОВАТЬСЯ' /> \
						</form>";
	
	form_block.appendChild(form);
	document.body.appendChild(background);
	document.body.appendChild(form_block);
	init();
	}

function delete_object(id, class_name){
	data = {id:id,class_name:class_name};
	$.ajax({
			url:"/library/delete",
			type:"POST",
			data:data,
			dataType:"json",
			success: load_control_form
			});
	}
	
function load_edit_form(id, class_name){
	data = {id:id,class_name:class_name};
	$.ajax({
		url:"/"+class_name+"/"+id,
		type:"POST",
		data:data,
		dataType:"json",
		success:show_edit_form
			});
	}
	
function show_edit_form(data){
	var background = document.createElement('div');
		background.id = "additional_background";
		background.onclick = function(){
			try	{
				var form_block = document.getElementById('additional_form_block')
				document.body.removeChild(form_block);
				document.body.removeChild(this);
			} catch(e){
			}
			}
	var form_block = document.createElement('div');
	form_block.id = "additional_form_block";
	var form = document.createElement('div');
	form.id = "additional_form";
	if (data['class_name'] == "Book"){
		form.innerHTML = "\
						<p>Форма редактирования:)</p>\
						<form action='/library/edit' method='POST' name='additional_form'>\
							"+reg_token+"\
							<input id='class_name' name='class_name' type='hidden' value='book'>\
							<input id='id' name='id' type='hidden' value='"+data['id']+"'>\
							<input id='name' name='name' type='text' value='"+data['fields']['name']+"'>\
							<input id='author_id' name='author_id' type='text' value='Айди автора: "+data['fields']['author']+"' onclick='this.value=\""+data['fields']['author']+"\"'>\
							<input name='button' type='submit' id='button' value='РЕДАКТИРОВАТЬ' /> \
						</form>";
		}
	if (data['class_name'] == "Author"){
		form.innerHTML = "\
						<p>Форма редактирования:)</p>\
						<form action='/library/edit' method='POST' name='additional_form'>\
							"+reg_token+"\
							<input id='class_name' name='class_name' type='hidden' value='author'>\
							<input id='id' name='id' type='hidden' value='"+data['id']+"'>\
							<input id='name' name='name' type='text' value='"+data['fields']['name']+"'>\
							<input id='second_name' name='second_name' type='text' value='"+data['fields']['second_name']+"'>\
							<input id='last_name' name='last_name' type='text' value='"+data['fields']['last_name']+"'>\
							<input name='button' type='submit' id='button' value='РЕДАКТИРОВАТЬ' /> \
						</form>";
		}
	form_block.appendChild(form);
	document.body.appendChild(background);
	document.body.appendChild(form_block);
	}
	
function edit_object(id, class_name){
	data = {id:id,class_name:class_name};
	$.ajax({
			url:"/library/delete",
			type:"POST",
			data:data,
			dataType:"json",
			success: load_control_form
			});
	}