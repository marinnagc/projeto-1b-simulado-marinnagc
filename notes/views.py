from django.shortcuts import render, redirect
from .models import Note, Tags, Fact

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag_name = request.POST.get('tag')
        tag_name = '#'+tag_name
        tag_exist = Tags.objects.filter(tag=tag_name)
        if not tag_exist:
            tag_exist = Tags.objects.create(tag=tag_name)
            tag_exist.save()
        elif tag_exist:
            tag_exist = tag_exist[0]
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        nova_nota = Note.objects.create(title=title, content=content,tag_id=tag_exist.id)
        nova_nota.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request,id):
    note = Note.objects.filter(id=id)
    note.delete()
    return redirect('index')

def editar(request, id):
    nota =Note.objects.get(id=id)

    if request.method == 'POST':
        novo_titulo = request.POST.get('titulo')
        novo_detalhe = request.POST.get('detalhes')
        #novo_tag_id = request.POST.get('tag')

        nota.title = novo_titulo
        nota.content = novo_detalhe
        #nota.tag.tag = novo_tag_id
        nota.save()

        # Se desejar, você pode redirecionar para outra página ou fazer outras ações após a atualização
        return redirect('index')

    return render(request, 'notes/editar.html', {'nota': nota})

def lista_tags(request):
    tags = Tags.objects.all()
    return render(request, 'notes/lista_tags.html', {'tags': tags})

'''def links(request, tag_nome):
    tag_resp = Tags.objects.get(tag=tag_nome)
    notas = Note.objects.filter(tag=tag_resp.id)
    return render(request, 'notes/notas_por_tag.html', {'links': notas})'''

def links(request,id):
    notas = Note.objects.filter(tag=id)
    #notas = Note.objects.filter(tag_id=id) FUNCIONA DOS DOIS JEITOS
    #print(notas[0].id,notas[0].title,notas[0].content)
    #print(notas[1].id,notas[1].title,notas[1].content)
    print(notas)
    return render(request, 'notes/notas_por_tag.html', {'links': notas})

def facts(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        novo_fato = Fact.objects.create(descricao=descricao,curtidas=0)
        novo_fato.save()
        return redirect('facts')
    else:
        fatos = Fact.objects.all()
        n_fatos = fatos.count()
        #n_fatos = len(fatos)
        return render(request, 'notes/facts.html', {'facts': fatos,'n_fatos':n_fatos})
    
def curtir(request,id):
    fact = Fact.objects.get(id=id)
    if request.method == 'POST':
        fact.curtidas = fact.curtidas+1
        return redirect('facts')
    else:
        fatos = Fact.objects.all()
        return render(request, 'notes/facts.html', {'facts': fatos})