function load_trends() {
    var trends = new Array();
    $.ajax({
        type: 'GET',
        url: "../Python/trends.py",
        //data: {"": "1"}, //passing some input here
        dataType: "text",
        success: function(response) {
            var json_trend = JSON.parse(response);
            var trend_str = '';
            for (var i = 0; i < json_trend.length; i++) {
                // check if there is a "#" in the topic, lead to different link
                // Show the Div of topic list.
                if (json_trend[i]["name"][0] == "#") {
                    trend_str += '<a href="https://twitter.com/hashtag/' + json_trend[i]["name"].split("#")[1] + '?src=tren" class="list-group-item">' + json_trend[i]["name"] + '</a>';
                } else {
                    trend_str += '<a href="https://twitter.com/search?q=%22' + encodeURIComponent(json_trend[i]["name"]) + '%22&src=tren" class="list-group-item">' + json_trend[i]["name"] + '</a>';
                }
                //show the topics in dropdown
                document.getElementById("topic_multi").options[i].innerHTML = json_trend[i]["name"];
            }
            document.getElementById("trend_list").innerHTML = trend_str;
            showtrends();
        }
    });
}

function update_dbTrends() {
    var r = confirm("Are you sure you need a update ?");
    if (!r) {
        return false;
    }
    $.ajax({
        type: 'GET',
        url: "../Python/update_trends_entry.py",
        dataType: "text",
        success: function(response) {
            alert("Updated the trends in database!");
            window.location.reload()
        }
    });
}

function collect_links() {
    // put section values into json format
    section_str = '[';
    for (var i = 0; i < $("#section_list :selected").length; i++) {
        section_str += '"' + $("#section_list :selected")[i].innerHTML + '",';
    }
    section_str = section_str.slice(0, [section_str.length - 1]) + ']'
        // check if selected one section
    if (section_str == "]") {
        alert("Choose one section please.");
        return false;
    }
    // alert(section_str);
    $.ajax({
        type: "POST",

        url: "../Python/collect_data_entry.py",
        datatype: "json",
        data: {
            'data': section_str
        },
        success: function(response) {
            alert(response.message);
        }
    });
}
function get_articles() {
    // put section values into json format
    section_str = '[';
    for (var i = 0; i < $("#trends_list :selected").length; i++) {
        section_str += '"' + $("#trends_list :selected")[i].innerHTML + '",';
    }
    section_str = section_str.slice(0, [section_str.length - 1]) + ']'
        // check if selected one section
    if (section_str == "]") {
        alert("Choose one section please.");
        return false;
    }
    $.ajax({
        type: "POST",
        url: "../Python/get_articles_entry.py",
        datatype: "json",
        data: {
            'data': section_str
        },
        success: function(response) {
            var articleStr = '';
            //alert(response.title.length);
            for (var i = 0; i < response.title.length; i++) {
                articleStr += '<tr><td>' + (i + 1) + '</td><td ><a href="' + response.url[i] + '">' + response.title[i] + '</a></td><td>' + response.tags[i] + '</td><td>' + response.section[i] + '</td></tr>';
            }
            location.href = "#article_table";
            document.getElementById('articles').innerHTML = articleStr;
            document.getElementById('article_table').className = "bs-example";
        }
    });
}
// search articles by user's key words
function user_search() {
    var key = document.getElementById("keyword").value;
    if (key.length < 3) {
        alert("Please put into a word more than 3 characters.")
        return false;
    }
    $.ajax({
        type: "POST",
        url: "../Python/user_articles_entry.py",
        datatype: "json",
        data: {
            'data': '["' + key + '"]'
        },
        success: function(response) {
            var articleStr = '';
            //alert(response.title.length);
            for (var i = 0; i < response.title.length; i++) {
                articleStr += '<tr><td>' + (i + 1) + '</td><td ><a href="' + response.url[i] + '">' + response.title[i] + '</a></td><td>' + response.tags[i] + '</td><td>' + response.section[i] + '</td></tr>';
            }
            location.href = "#article_table";
            document.getElementById('articles').innerHTML = articleStr;
            document.getElementById('article_table').className = "bs-example";
        }
    });
}