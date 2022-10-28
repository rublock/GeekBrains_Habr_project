const autoCompleteJS = new autoComplete({
    name: 'autoComplete',
    selector: '#autoComplete',
    wrapper: false,
    debounce: 300,
    threshold: 3,
    submit: false,
    placeHolder: 'Поиск...',
    searchEngine: 'loose',
    diacritics: true, // поиск по букве Ё
    data: {
        cache: false,
        src: async (query) => {
            try {
                const source = await fetch(`/search-post-json/?search=${encodeURI(query)}`);
                const data = await source.json();
                return data;
            } catch (error) {
                return error;
            }
        },
        keys: ['title']
    },
    events: {
        input: {
            focus() {
                const inputValue = autoCompleteJS.input.value;
                if (inputValue.length) autoCompleteJS.start();
            },
            selection(event) {
                const selection = event.detail.selection.value
                autoCompleteJS.input.value = selection.title;
                window.location.href = `/posts/${encodeURI(selection.id)}/`;
            },
            keydown(event) {
                if (event.key === 'Enter') {
                    window.location.href = `/?search=${encodeURI(autoCompleteJS.input.value)}`;
                }
            }
        },
    },
    resultsList: {
        tag: 'ul',
        id: 'autoComplete_list_[id]',
        //class: '',
        destination: '#autoComplete',
        position: 'afterend',
        maxResults: 10,
        noResults: true,
        element: (list, data) => {
            if (!data.results.length) {
                const message = document.createElement('div');
                message.classList.add('no_result');
                message.innerHTML = 'Ничего не найдено';
                list.appendChild(message);
            }
        },
},
    resultItem: {
        tag: 'li',
        id: 'autoComplete_result_[index]',
        //class: '',
        highlight: true,
        //selected: '',
    },
});
