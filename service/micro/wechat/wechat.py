


from bs4 import BeautifulSoup

aaa = """
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0,viewport-fit=cover">
<link rel="shortcut icon" type="image/x-icon" href="//res.wx.qq.com/a/wx_fed/assets/res/NTI4MWU5.ico">
<link rel="mask-icon" href="//res.wx.qq.com/a/wx_fed/assets/res/MjliNWVm.svg" color="#4C4C4C">
<link rel="apple-touch-icon-precomposed" href="//res.wx.qq.com/a/wx_fed/assets/res/OTE0YTAw.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="color-scheme" content="light dark">
<meta name="format-detection" content="telephone=no">


        

  
  <meta name="description" content="" />
  <meta name="author" content="" />

  
  <meta property="og:title" content="这名99后跳下冰河冻得呻吟发抖，他却说......" />
  <meta property="og:url" content="http://mp.weixin.qq.com/s?__biz=MjM5NDg5MjExMQ==&amp;mid=2650775174&amp;idx=1&amp;sn=763df4247d40384132e0a6b5361275a5&amp;chksm=be8beea689fc67b0c2feaa4223410378b28c0f1d3ee99c033c89d499ce2c205e4c07a3b95224#rd" />
  <meta property="og:image" content="http://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdk53oez8Pp9VkYy0xF8GxicvW0XDZBvsakC8qgyAXD8aFVTy868wRNJ9A/0?wx_fmt=jpeg" />
  <meta property="og:description" content="" />
  <meta property="og:site_name" content="微信公众平台" />
  <meta property="og:type" content="article" />
  <meta property="og:article:author" content="" />

  
  <meta property="twitter:card" content="summary" />
  <meta property="twitter:image" content="http://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdk53oez8Pp9VkYy0xF8GxicvW0XDZBvsakC8qgyAXD8aFVTy868wRNJ9A/0?wx_fmt=jpeg" />
  <meta property="twitter:title" content="这名99后跳下冰河冻得呻吟发抖，他却说......" />
  <meta property="twitter:creator" content="" />
  <meta property="twitter:site" content="微信公众平台" />
  <meta property="twitter:description" content="" />


        <script nonce="567503264" type="text/javascript">
            window.logs = {
                pagetime: {}
            };
            window.logs.pagetime['html_begin'] = (+new Date());
            window.LANG= "zh_CN"; 
        </script>
        <title>
</title>
        <!---请求录制 by gabyliu-->
                
<style>.radius_avatar{display:inline-block;background-color:#fff;padding:3px;border-radius:50%;-moz-border-radius:50%;-webkit-border-radius:50%;overflow:hidden;vertical-align:middle}.radius_avatar img{display:block;width:100%;height:100%;border-radius:50%;-moz-border-radius:50%;-webkit-border-radius:50%;background-color:#eee}.rich_media_inner{word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto}.rich_media_area_primary{padding:20px 16px 12px;padding:calc(20px + constant(safe-area-inset-top)) calc(16px + constant(safe-area-inset-right)) 12px calc(16px + constant(safe-area-inset-left));padding:calc(20px + env(safe-area-inset-top)) calc(16px + env(safe-area-inset-right)) 12px calc(16px + env(safe-area-inset-left));background-color:#fafafa}.rich_media_area_primary.voice{padding-top:66px}.rich_media_area_primary .weui-loadmore_line{border-color:#d8d8d8}.rich_media_area_primary .weui-loadmore_line .weui-loadmore__tips{color:#888;background-color:#fafafa}.rich_media_area_extra{padding:0 16px 16px;padding:0 calc(16px + constant(safe-area-inset-right)) calc(16px + constant(safe-area-inset-bottom)) calc(16px + constant(safe-area-inset-left));padding:0 calc(16px + env(safe-area-inset-right)) calc(16px + env(safe-area-inset-bottom)) calc(16px + env(safe-area-inset-left))}.rich_media_extra{padding-top:30px}.mpda_bottom_container .rich_media_extra{padding-top:24px}.mpda_bottom_container .rich_media_extra .mpad_more_list{right:-10px}html{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;line-height:1.6}body{-webkit-touch-callout:none;font-family:-apple-system-font,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Hiragino Sans GB","Microsoft YaHei UI","Microsoft YaHei",Arial,sans-serif;color:#333;background-color:#f2f2f2;letter-spacing:.034em}h1,h2,h3,h4,h5,h6{font-weight:400;font-size:16px}*{margin:0;padding:0}a{color:#576b95;text-decoration:none;-webkit-tap-highlight-color:rgba(0,0,0,0)}.rich_media_title{font-size:22px;line-height:1.4;margin-bottom:14px}@supports(-webkit-overflow-scrolling:touch){.rich_media_title{font-weight:700}}.rich_media_meta_list{margin-bottom:22px;line-height:20px;font-size:0;word-wrap:break-word;word-break:break-all}.rich_media_meta_list em{font-style:normal}.rich_media_meta{display:inline-block;vertical-align:middle;margin:0 10px 10px 0;font-size:15px;-webkit-tap-highlight-color:rgba(0,0,0,0)}.rich_media_meta.icon_appmsg_tag{margin-right:4px}.rich_media_meta.appmsg_title_tag{margin-right:8px}.rich_media_meta.meta_tag_text{margin-right:0}.rich_media_meta_primary{display:block;margin-bottom:10px;font-size:15px}.meta_original_tag{padding:0 .5em;font-size:12px;line-height:1.4;background-color:#f2f2f2;color:#888}.meta_enterprise_tag img{width:30px;height:30px!important;display:block;position:relative;margin-top:-3px;border:0}.rich_media_meta_link{color:#576b95}.rich_media_meta_text{color:rgba(0,0,0,0.3)}.rich_media_meta_text.rich_media_meta_split{padding-left:10px}.rich_media_meta_text.rich_media_meta_split:before{position:absolute;top:50%;left:0;margin-top:-6px;content:' ';display:block;border-left:1px solid #888;width:200%;height:130%;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:0 0;transform-origin:0 0}.rich_media_meta_text.article_modify_tag{position:relative}.rich_media_meta_nickname{position:relative}.rich_media_thumb_wrp{margin-bottom:6px}.rich_media_thumb_wrp .original_img_wrp{display:block}.rich_media_thumb{display:block;width:100%}.rich_media_content{overflow:hidden;color:#333;font-size:17px;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto;text-align:justify;position:relative;z-index:0}.rich_media_content *{max-width:100%!important;box-sizing:border-box!important;-webkit-box-sizing:border-box!important;word-wrap:break-word!important}.rich_media_content p{clear:both;min-height:1em}.rich_media_content em{font-style:italic}.rich_media_content fieldset{min-width:0}.rich_media_content .list-paddingleft-1,.rich_media_content .list-paddingleft-2,.rich_media_content .list-paddingleft-3{padding-left:2.2em}.rich_media_content .list-paddingleft-1 .list-paddingleft-2,.rich_media_content .list-paddingleft-2 .list-paddingleft-2,.rich_media_content .list-paddingleft-3 .list-paddingleft-2{padding-left:30px}.rich_media_content .list-paddingleft-1{padding-left:1.2em}.rich_media_content .list-paddingleft-3{padding-left:3.2em}.rich_media_content .code-snippet,.rich_media_content .code-snippet__fix{max-width:1000%!important}.rich_media_content .code-snippet *,.rich_media_content .code-snippet__fix *{max-width:1000%!important}.rich_media_content img{height:auto!important}@media screen and (min-width:1024px){.rich_media_area_primary_inner,.rich_media_area_extra_inner{max-width:677px;margin-left:auto;margin-right:auto}.rich_media_area_primary{padding-top:32px}}blockquote{padding-left:10px;border-left:3px solid #dbdbdb;color:rgba(0,0,0,0.5);font-size:15px;padding-top:4px;margin:1em 0}.blockquote_info{color:rgba(0,0,0,0.3);margin-top:1.17647059em;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto}.blockquote_article{display:block}.appmsg_share_notice{font-size:16px;color:#888;position:relative;padding:1.25em 0;margin-bottom:1.75em}.appmsg_share_notice:before{content:" ";position:absolute;left:0;top:0;right:0;height:1px;border-top:1px solid #dfdfdf;-webkit-transform-origin:0 0;transform-origin:0 0;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.appmsg_share_notice:after{content:" ";position:absolute;left:0;bottom:0;right:0;height:1px;border-bottom:1px solid #dfdfdf;-webkit-transform-origin:0 100%;transform-origin:0 100%;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.appmsg_share_notice_hd{font-weight:700;padding-bottom:.2em}.dn{display:none}.qa__card{background-color:#fafafa;border-radius:4px;padding:20px;position:relative;margin:8px 0}.qa__card::before{content:"";display:block;position:absolute;width:24px;height:24px;background-size:cover;background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='5857326e-0388-4946-90a6-c4e335712b3a-a' d='M14.706 12.611l-.147.004c-.461 0-.748-.362-.568-.767a.945.945 0 0 1 .663-.533c.652-.158 1.09-.662 1.09-1.245 0-.705-.682-1.289-1.545-1.289-.862 0-1.546.584-1.546 1.29v3.859c0 1.426-1.269 2.57-2.826 2.57C8.269 16.5 7 15.356 7 13.93c0-1.252.984-2.316 2.338-2.52h.103c.35 0 .615.221.615.538a.573.573 0 0 1-.007.107.429.429 0 0 1-.04.123c-.107.25-.373.46-.663.533-.648.156-1.09.658-1.09 1.219 0 .705.682 1.289 1.545 1.289.862 0 1.546-.584 1.546-1.29V10.07c0-1.426 1.269-2.57 2.826-2.57C15.731 7.5 17 8.644 17 10.07c0 1.257-.96 2.31-2.294 2.541z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath fill='%23FFF' fill-opacity='.9' stroke='%23000' stroke-opacity='.05' stroke-width='.5' d='M12 22.75c5.937 0 10.75-4.813 10.75-10.75S17.937 1.25 12 1.25 1.25 6.063 1.25 12 6.063 22.75 12 22.75z'/%3E    %3Cuse fill='%236467F0' xlink:href='%235857326e-0388-4946-90a6-c4e335712b3a-a'/%3E    %3Cuse fill='%23FFF' fill-opacity='.2' xlink:href='%235857326e-0388-4946-90a6-c4e335712b3a-a'/%3E  %3C/g%3E%3C/svg%3E");right:8px;top:8px}.qa__card-hd{font-size:14px;color:rgba(0,0,0,0.5);margin-bottom:8px}.qa__card-hd span{margin-right:5px}.qa__card-desc{line-height:24px;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}.qa__card-bd{margin-bottom:12px}.qa__card-bd:last-child{margin-bottom:0}.qa__card-ft{font-size:14px;color:rgba(0,0,0,0.5)}.qa__card-ft span{margin-right:12px}.qa__card-theme{font-size:18px;font-weight:500;line-height:30.8px}.qa__icon-qa{display:inline-block;vertical-align:-4px;width:20px;height:20px;background-size:cover;background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20'%3E  %3Cg fill='%23F7F7F7'%3E    %3Cpath d='M11.938 16.083l-.007.102a.75.75 0 0 1-.743.648H9.562a.75.75 0 0 1-.75-.75h3.126zm0-2.5l-.007.102a.75.75 0 0 1-.642.641l-.101.007H9.562a.75.75 0 0 1-.743-.648l-.007-.102h3.126zm-1.563-10.25a5.375 5.375 0 0 1 4.341 8.545l-.159.207-.583-.472a4.625 4.625 0 1 0-7.363-.216l.158.208-.584.47a5.375 5.375 0 0 1 4.19-8.742z'/%3E    %3Cpath d='M10.453 6.833c.6 0 1.088.16 1.444.497.347.319.525.76.525 1.322 0 .422-.122.788-.347 1.097-.094.112-.356.356-.769.722a1.882 1.882 0 0 0-.431.506 1.34 1.34 0 0 0-.178.694v.215h-.76v-.215c0-.31.057-.581.179-.816.122-.281.44-.637.947-1.087.15-.15.253-.263.318-.338.178-.234.272-.478.272-.74 0-.375-.103-.666-.31-.872-.224-.225-.534-.328-.927-.328-.46 0-.807.15-1.041.459-.197.262-.3.619-.3 1.078h-.75c0-.656.188-1.181.553-1.575.384-.412.91-.619 1.575-.619z'/%3E  %3C/g%3E%3C/svg%3E")}.weui-btn_primary.qa__btn{position:absolute;right:15px;bottom:20px;width:111px;padding:8px 0}.qa__card_v2 .weui-btn_primary.qa__btn{bottom:32px}.qa__card_v2 .qa__card-bd{margin-bottom:6px}.qa__card-content{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.qa__card-avatar{width:48px;height:48px;border-radius:50%;overflow:hidden;margin-right:8px;-webkit-flex-shrink:0;flex-shrink:0}.qa__card-avatar img{width:100%}.qa__card-main{overflow:hidden;-webkit-box-flex:1;-webkit-flex:1;flex:1}.qa__card-main-name{font-weight:500;line-height:27.2px;margin-bottom:2px;margin-right:120px;white-space:nowrap;text-overflow:ellipsis;overflow:hidden}.qa__card-main-info{font-size:14px;color:rgba(0,0,0,0.5);line-height:17px}.qa__card-main-info span{margin-right:5px}.qa__card_v3{padding:21px 16px}.code-snippet{margin:10px 0;display:block;overflow-x:auto;font-size:14px;padding:1em 1em 1em 3em;color:#333;position:relative;background-color:#fafafa;border:1px solid #f0f0f0;border-radius:2px;counter-reset:line;white-space:normal;-webkit-overflow-scrolling:touch}.code-snippet code{text-align:left;font-size:14px;display:block;white-space:pre-wrap;position:relative;font-family:Consolas,"Liberation Mono",Menlo,Courier,monospace}.code-snippet code::before{position:absolute;min-width:1.5em;text-align:right;left:-2.5em;counter-increment:line;content:counter(line);display:inline;margin-right:12px;color:rgba(0,0,0,0.15)}.code-snippet_nowrap code{white-space:pre;display:-webkit-box;display:-webkit-flex;display:flex}.code-snippet__fix{font-size:14px;margin:10px 0;display:block;color:#333;position:relative;background-color:rgba(0,0,0,0.03);border:1px solid #f0f0f0;border-radius:2px;display:-webkit-box;display:-webkit-flex;display:flex;line-height:26px}.code-snippet__fix pre{overflow-x:auto;padding:1em;padding-left:0;white-space:normal;-webkit-box-flex:1;-webkit-flex:1;flex:1;-webkit-overflow-scrolling:touch}.code-snippet__fix code{text-align:left;font-size:14px;display:block;white-space:pre;display:-webkit-box;display:-webkit-flex;display:flex;position:relative;font-family:Consolas,"Liberation Mono",Menlo,Courier,monospace}.code-snippet__fix .code-snippet__line-index{counter-reset:line;-webkit-flex-shrink:0;flex-shrink:0;height:100%;padding:1em;list-style-type:none}.code-snippet__fix .code-snippet__line-index li{list-style-type:none;text-align:right}.code-snippet__fix .code-snippet__line-index li::before{min-width:1.5em;text-align:right;left:-2.5em;counter-increment:line;content:counter(line);display:inline;color:rgba(0,0,0,0.15)}.code-snippet__comment,.code-snippet__quote{color:#afafaf;font-style:italic}.code-snippet__keyword,.code-snippet__selector-tag,.code-snippet__subst{color:#ca7d37}.code-snippet__number,.code-snippet__literal,.code-snippet__variable,.code-snippet__template-variable,.code-snippet__tag .code-snippet__attr{color:#0e9ce5}.code-snippet__string,.code-snippet__doctag{color:#d14}.code-snippet__title,.code-snippet__section,.code-snippet__selector-id{color:#d14}.code-snippet__subst{font-weight:normal}.code-snippet__type,.code-snippet__class .code-snippet__title{color:#0e9ce5}.code-snippet__tag,.code-snippet__name,.code-snippet__attribute{color:#0e9ce5;font-weight:normal}.code-snippet__regexp,.code-snippet__link{color:#ca7d37}.code-snippet__symbol,.code-snippet__bullet{color:#d14}.code-snippet__built_in,.code-snippet__builtin-name{color:#ca7d37}.code-snippet__meta{color:#afafaf}.code-snippet__deletion{background:#fdd}.code-snippet__addition{background:#dfd}.code-snippet__emphasis{font-style:italic}.code-snippet__strong{font-weight:bold}.cell{padding:.8em 0;display:block;position:relative}.cell_hd,.cell_bd,.cell_ft{display:table-cell;vertical-align:middle;word-wrap:break-word;word-break:break-all;white-space:nowrap}.cell_primary{width:2000px;white-space:normal}.flex_cell{padding:10px 0;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.flex_cell_primary{width:100%;-webkit-box-flex:1;-webkit-flex:1;box-flex:1;flex:1}.original_tool_area{display:block;padding:.75em 1em 0;-webkit-tap-highlight-color:rgba(0,0,0,0);color:#333;border:1px solid #eaeaea;margin:20px 0}.original_tool_area .tips_global{position:relative;padding-bottom:.5em;font-size:15px}.original_tool_area .tips_global:after{content:" ";position:absolute;left:0;bottom:0;right:0;height:1px;border-bottom:1px solid #dbdbdb;-webkit-transform-origin:0 100%;transform-origin:0 100%;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.original_tool_area .radius_avatar{width:27px;height:27px;padding:0;margin-right:.5em}.original_tool_area .radius_avatar img{height:100%!important}.original_tool_area .flex_cell_bd{width:auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-wrap:normal}.original_tool_area .flex_cell_ft{font-size:14px;color:#888;padding-left:1em;white-space:nowrap}.original_tool_area .icon_access:after{content:" ";display:inline-block;height:8px;width:8px;border-width:1px 1px 0 0;border-color:#cbcad0;border-style:solid;transform:matrix(0.71,0.71,-0.71,0.71,0,0);-ms-transform:matrix(0.71,0.71,-0.71,0.71,0,0);-webkit-transform:matrix(0.71,0.71,-0.71,0.71,0,0);position:relative;top:-2px;top:-1px}.rich_media_global_msg{position:fixed;top:0;left:0;right:0;padding:.85em 35px .85em 15px;z-index:2;background-color:#c6e0f8;color:#888;font-size:12px}.rich_media_global_msg .icon_closed{position:absolute;right:15px;top:50%;margin-top:-5px;line-height:300px;overflow:hidden;-webkit-tap-highlight-color:rgba(0,0,0,0);background:transparent url(//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg/icon_appmsg_msg_closed_sprite.2x42f400.png) no-repeat 0 0;width:11px;height:11px;vertical-align:middle;display:inline-block;background-size:100% auto}.rich_media_global_msg .icon_closed:active{background-position:0 -17px}.rich_media_global_msg.voice{color:#1aad19;background-color:#e8f6e8;padding-left:43.3px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.rich_media_global_msg.voice .ic_voice{position:absolute;top:50%;margin-top:-10px;left:15px;display:inline-block;width:13.3px;height:18.3px;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAA3CAYAAAB+fggjAAAAAXNSR0IArs4c6QAACb9JREFUaAW9WX9wVMUd3917d5cf/Agp1OTuQgIlQqUoI1JI1Noojg2I+VU7hVrtDDpadRypgzKjU52x09KOdsS20ypSO/WPWttcAqhTOlSoU4FIoRUn0wEZIMndBUkwGEhyv97bfvaS97L77t3lHYUuc+z3935397vf/e4LJZfQnuPPsW0d25ZQzr9mELKSUnIVzHxB/Dh+lBOKf4OEk0FOyQAl/CyltIt5tL29d/V2FzIkLUQ4FA7dwon+KCF0Fee8rBBdS5aSs/D+PUrYbyKtkb9b9BzAlA7CERrqDN1DOH8C8HU57FwSGat6kBGypbcluhMwFj+75XWwemf1vHQqtZ0T3pCtelkp73uJ79s9bT39dqs5HQyFK79jcPIKFErtSgLHjPvQHQB0EFt2hDE2QHU6RMvpkODrw3o50Uk5p3w2N/SlUKhHTNZjskHBz2pi6ylbH22J/k3mOToYCAceIYT/AgYVPhxJQTkMQ792Ez/yQCY8d0fgRl0nj8J2G5z1mvSJ3qCMrYOTb5l0xQFBDIUDjxmcbzUFJnu621/kf/DUmlM9k7RLh4LtwRChxquck0bFCqWjxENuijXF/iXoioNVnZU36wZ5D7PTTCWsWhyp4uFYa+x1k3Y5ezj6oNgtdTVpL0Lo+mhr9BwO0Xib+/bcWYZB35Sdg/sXsOSNV8o5MXK0LfoKYXQDxpJOMZ8L1g8E33JQT6aeQRoJCOJEMxjxfCvSEtlnEq5Uj5h7Ayv2I8U+5w9du/va0oyD896ZV004RQKebIzQ53EQ/jJJubJQhUa2YBXPmqNgy8vPjZ67N+NgMh6/HwSfyURgniwqLvmJif8/+sNrY6O4XV5WxjKMuvHDQOl9uCksHmX0xydWn0hYBJfAgncXzBhNjjZSnX8Fq3ENdmWWUMUhS2Ebv5HrtjDNg/+B5IY4wos0cVukUskqUwj9xfKS2W9GSEwi5QdxFS5BMn54dGzkHkhOy0x18j9COY1O5VxmhGJylIxMjgUTC7WUkfrqJAkQpfuP3nFUElO4WUgwHHza0HU1wG1SGOi0jeSI+kf92hgZlXg0yajBV0gUwri4vqZud/O7PbhxkGiNvM5NWHKV3NN8LGQbuVdDsYIVzOzHOI+ygzYhR/RAxwdbELcPZDEp+Q+2YQcS2L+Zwc4gdSUQS7Oz5BwIKUqWyq5ApEdDsVmhBKaHnHDQVUg1uwKLkkm+USEScsbjId/ra+7fbaMThMHVdpoTjuyxXloqcUg+Eqe4WBb26/5hGXeCkynyfdA9Fo/SQeZlN/StjUQtmgQUFxVnKhyJlAUGOgP13OC3ygxGWZhhSYtkYqIicUHGnWCUluoFz8mzkRzOCf14Wfyikx2ThvQ0B6XZdvhi1QaoAfZHmiMf40xMJmih4BvxWQnbNCD3i/cunoYab4FMQwr5o4zb4Uh9ZMxOM3Fsf91YfPQfOAeLTJrouYc8K3rEII0ikBcKRLTEhUQNuo8E7NSGh4dnyDOFzIioOpxkZdqyXYGSAV2rMYjhIUamkL2ZcANvG+MWWS4DU/parDm2R8AiBj/Bz3IQe14DPKeDRho1hNyonFplhgp/mmaNhpH6s0VVToNFxR7TPcVFJVZdgMG4cNBq0LvRQhyA2vLaMyDrFouTL169KzBlGkEofdnScQYMXBI/raiuXC1fs4wz2iXLI+U0y7gd3tewL41IVhLvmM6X2eWycM7nZ9EEAXWgWDWPpjWg7tx8+IbD4llhNTadTn8XcWgVBphprbhbLQkngJK/ymTdoE/IuDPME5jYSYx1HLn3EH6/B77Rq/m+FG2L3d7X1Pe+kx5kCBJp4G0clDWmAJTD0db+NhO398GO4G3cMDJBbPIY9bShfgyb+OXqMwGPV9rrskFsc6t4fck0GRZPQ5GnZBpO4x/wvrAmKfP+FzjjYF9zn5i58s0ET8MX8hnGc+BxOGnFi8innBg7UUBsFaV6Pt1CeBMrKD73qG8CbPnKUHvg/lzG+tr6DlGWufJkEWQp/tjgyMBJPF+fWrhj4XSZeSlwJgaFIhyioY7gHvS3moYyK6TRO6JN0b0mzd6HOgIbEBK/gp7fzsOBGMLUX2Z+bWvvnb1T3sd2fYFbDgoET8/56UTqKEBrizDIeY1463tae1BGObeq9qrlBtXb4aRcmVvCmOjneFq+UFZW9lJ3Q3fee9lSmgAUBwUNd+N9CPjfTfDHO0pO+z1FK081nfpUoUuIuKPPD322Gav5OMjWBCURRBGN4GH0QCGvxSwHhcFguPLnGEip97AKXd5y39dPN5yOy4PaYXGrjKToRsTMIzg4M+38cZz+LNYWe8qZp1Izh0QlEVLfctMmzNb6gCP4GGxFcij5W7usHT++NjaI4uHpadr0KkbpZvAH7DKw9iRi98lsejbFcQWF2LJ/LvOe6Yl14m5eLavhU8gqkQdlWj5YnOSL+sXNWNFNmKT1NQsLkGAez3zcIHmfj44rKAYUd2Jxcek6HCP1cHD+Ig5DzonZnT3WdOyCWFGukRUIwkGTL069kdYz319MmlOf00EhjKpiWKPku7IiDF9X3RHMecvIsjIsPqdh1ewO3SXLOMF5HRQKvS39h5GNOmVlnZP1Mu4W9pZ5/4TDZh0ybHkt3iKOqcm0OaWDQpB52DZTQfQo+Vtl3C08kQGO2OStYtlGz6CuHJxZO3MPYnHYMsDJVSKpW3ghAOXKsxaPoup86q4c7F7cncSyHZANGen0Shl3C+PSPy/L4qmZ97525aAwiMLgQ8Uwp8tl3C2MASff00KJMRW3GXLtIFbwY1kXp/kaGXcL42AoDqHit6p5JxuuHfQwj1IvIhFO9QhyGk/QpskM/C3Gyo0y3YRdOzgnNOcTHJS0qYgVrBIfLE28gF75ToN3bySfrmsHM68tTo7JxuKJ+PUyPhWcqbQ5XarI+TRlZxQeENcOjitS5dMc5/oqu8F8+ODI4FrEoPVpBTfL8akK2YIc9DCiFAkoyTbUdNSU5XPK5Im/MQPeZOKZnpNdCu6AFOTgrJLZO2FDrogrUjyxPbQ/VOxgWyG9Fn71h6hoJkMC8exlvl8qQg6I66rE1A22Vz6PEuwZExe92CrQtmmU72U+fzQ9K/15XV1dsuudrhlc50t0XX8Izq1TdAh5I9rWf69Mc4ILdlCU9kNDn32ICvZS0wySAY2W+shSUdw6OSXTCtpioSgePZrPeydWTUncstF8MPRw1dFvunFO2CnYQaGEk3cSn8iWYyVeBGoImqtG6RHxQsQfEJVskE+34C22GxOfb8fiY40owtaAJ0qnciTxcvSlE7VfBPX3IQ8lb/U2R3dgBRGu7tt/AYJkZEGv/oaXAAAAAElFTkSuQmCC) no-repeat center;background-size:contain}.rich_media_global_msg.voice .icon_more{position:absolute;right:15px;top:50%;margin-top:-6.5px;width:8px;height:13px;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAmCAYAAADeB1slAAAAAXNSR0IArs4c6QAAA49JREFUSA2tVk1IVFEUPveOmhQk1ibfvLFZSJtACqJIIpCIoB+imcFV2Z9ZUVnRomgRGFn2i6mFf5XVotCZMYmgIMhlq6BFENFiwjfPAosgFzXOvNu5o3fmeue98Y16F3PP+c453/fu/xCQmvZSWwwJaC0G6P8WND9IoTmbVFRycpqAdgBWkwRo94V960RsPn1aoPpN9RI6CR0WsDWcjAErtUiqTR/S18+HnNcSTv5zYrwDSatVMgLkH6aciwfj79WYW5+OT4xfsyPnBIgvwt872qBW45ZQzaMlJXCfMPJbDQgfRUoIhduVUW2TwArpaWyX+bnYU9JAAH44FaJIccqCW76Ib7NTjhOOvFPN/8q/IvE3cR+npFJgao9rkiSUXjD2GCNqzMnPbNPYjth3mqINlJAvTsk4kiJmWa3eQe8WpxwVzwjwgFFn/CorL29EkY9qovC5CFDrKq7JVoHl6zNTJCf53/lLk78SN/FcbJRx2cZCixC4ZATGXsu4as8YgQjGamN/q5atOotn4K3A1J4BUMbgsh7Wt6sx2bcV4AkjtSPJxkDjRQL0hVwg21zEglSzN+rdKeOybTtFcgK39ajWZDFWr+IZHxfGQ8mV0YA5nMGmDVcCPNcb8R5gYJ1UCWQfp6PFCI4NyZhrAV6EIiHGrPOAB0ImkW2c0la8u8ICc0wUCWrvC1dsw+3TnN6uanDaJ4zeiIfiA9wtWIAX8XspxeA6iuBlaN88hNzCNXk+JwFOuXJYW5tMQmc+EcqgzXGb2n9XFk1NstX5yKczl89JAF+6vRaBM1m5XAu//qkRGrtb8BThTtqH2/V0LmUWwbvsiREw8X0vcJHxxNbjNm3KUuVaMjmPFuWm2CPesHc/kp+yj06hFMhj/PIOOcfVFLk6xZT0G3vMTpmc27MusityZk/OBfKOwA05MPLIDJn3OJldcxTQotpBYOyEXVEWIw/NoInvuHOznSJfVDs0GzneNw9mI+eyOSPQI9phfCqPO38TFhHaFw/Eu/LliNiMESB5w6zkzD05F8mMYJr8mFC263Fa+vAadvXloj4toEcrjlgMjgrQrseHpBcfkm67WD6M6MN6lTWZeoZjyYxGLcB57MGnsEfF3fjU2G189QBpcUqmBLrnSs4504s8GjLxrwm5qYrg3dKFf6x6VbwQ3yOS/wz8+bS0ruwfELaBY2nyoNkn4gvW65GKRn4WForwP+dONHDaOHeZAAAAAElFTkSuQmCC) no-repeat center;background-size:contain}.preview_appmsg .rich_media_title{margin-top:2.3em}@media screen and (min-width:1024px){.rich_media_global_msg{position:relative;margin-bottom:32px}.preview_appmsg .rich_media_title.rich_media_title{margin-top:0}}.pages_reset{color:#333;line-height:1.6;font-size:16px;font-weight:400;font-style:normal;text-indent:0;letter-spacing:normal;text-align:left;text-decoration:none;white-space:normal}.weapp_element,.weapp_display_element,.mp-miniprogram{display:block;margin:1em 0}.share_audio_context{margin:16px 0}.weapp_text_link{font-size:17px}.weapp_text_link:before{content:'';display:inline-block;line-height:1;background-size:contain;background-repeat:no-repeat;background-image:url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAB4RJREFUWAm1WUuMFGUQnn7szL5mdvbh7GwgEQUlS1weiagxxpigiUZeJgY1cMMDcDCGG8GLCWZvxHjh4BWUeDEsejBBEzWYKBBEiHAABBfCMOwsuzvszrvb+v6Zb7amt1ce0Up6qv6q+qq+/rv778dYkUeUqamp5dFodJPv++ts205blpX2PG8I5cTOiLol44zYZ8vl8vFkMnnlUVpZDwPK5/MpIbWrVqttFlLD0jwiBEHIaNbCGKJjQvai+I9Xq9VD8Xg8y9z76QcimM1mu3t6ej4UYh84jtOFxhBNJGxskhp5xIielZ37bHp6+tNUKnWPOYvp+xKcm5t7S4gclKIpFNGzsmjRkBnUOwNbZjQrtfZ2dnZ+vVgd+O1/CVqlUukjIXZYCqZADBuEJIllc4xh61zmaB9s7LDkHkYPwJgX1KEEx8fHO2TmjkjyPgLQmERIAjHajGnyjDGPOfQ3xvvQCz3ZS+sw5hYAsodbWBhNw4SNGCMBnR/MYS60jskhPyaHe7u4W5otmEGZ8v0gx2YsyDE0bc4Wx8glOe2Dn2No2hqPnuiNXC0tM9i4IA5LcksjNm0BNs417aMNAsRom3HoMD8wsu3QF06TIJaSRCJxXrDmamUBrVEYRejDmDY0JEgsLE4f8mkTj6tb1tsRLkEukiBY56Q4rizThI2okaNtjFlUx+Cr1vzIyTMz7uW/ik4mV7Yd24oMDrR5q1Z01Nav6a5yVsLwcvRS4CI1D5ge+MEdQhbgC1yECSQhjMNsYCGMQ2dzFeuLYxOxibuVBec3cpekY7XtWwZK8a75sMajj2yzcsd5BnccM4PCeg/JoQjJwAY4TFgUMeRjXK54kS/H6uR6e1xvw4vJyuNLYh5yrt8s2d//MtV2M1Nyvvo2F9u5LVUSJEJNPPtKrS7XdXdL6GOzG+LYqIJNUiShYyRDjRw2OXnmnntnsmInE663e3u6uHZVZy2ZsH1sa4Y7ant2DBURu3aj6Jz9c9YBVuNRhz6pvwlju1gsPikzaG78CKIxNgh1sAj91MhFztXrRQf2C+vi1Y721tMC/vZYPQb78rWCE8Tr/uCEJyZbrprNAAST4QOAIGj6qBnDGPjZgmeS0gNRc1jD8D1xx+y978/XJh4awl54nHOl8Do6STKoDarxg5gmxpj2yTEwbtZhDvSlKwUzy+lU1NPxFvz8EcSzpnnYXDCD3AtqFtOFGNM+kMBYx+DzPD/y86m8e+7SnBON2v7qlR01ncP6Gg9uriSlGSSAYyTDhl/7bmTK9tXxkj3ydFetL4lTqT5jyIdgTB/0qT9m3R9/zbvT+Yottfw3XuktJxP1Q61rh/QfcuUcHBKmzcIwdCILQE/crVpHj9+JZe7U17hSyau89lJPxYDVD3KJm5qpWWMnJqMIY+nZvKGv/NQT7ebwcicI5RhYiHBLYx30WQxObWNMyQm5Q0cy7ULK6up0/PUj3dWXn48bckEMGrGZkPJ3bhssunLmLR2qXzyIacxitvT2XZm9jABWMEmD6QPJYzILILdyeWf13Y39ZTSEMAeaQpuxZUujHn26fhCPmI6Dmy0OvIE1AyyqfYWiH7n6d9GJxWz/7df7FpBjLjQETag1Me1HPKxXwJfByXeLRViUYGiI3F/NSYr1raPdNoXh594S75nVT1Z/mUz6kAfhGJp2EI887gRy5Bw0M/g7ndQI0gZISJkpyU6WbTm7m8RYELnFkh+ZnK4/qCTiWF4XXtk6X5NkLjX7iz4rh9keAxBODaKNWKrf9Qd627yC3Cm++2m6DbHWYpHI2Im7UfFZqf6oN9DrmAsPWIquH8QjR8dRG2O88JszW56kTwvRYSayOYtD37xdsT8/ejtWq/nWsqXttdXDHdW+RNTHY9Vv5/IuTgPHtfxd7w0V04/V1ziND5IiCeTofsyTw3tRnqyfNY9b8qg1JkktXwo0EKAlg23eO2/2l7/5YaoNTyPYNIFEt6xxr/aVQQ75QTxJkEBYnDFocEKOqYQHVnn+uiCBLji1IBnCBiVZ+U6fv+dmshV7cqpq9fY4/tBg1HtudXe1zeyuRs9fHMRrEvQBQT9smb1Z+YphHljr3cWJF2gB7NOENAhAjrWGP9iIPuZhDOFYa/hD8KOxWOyAweAHEnxpqnvrvyyofbQZg4boZsEcjrUO4mX2Wl6a6jdhQeAtSoJ70YDNoIMFwmJoqImF5Wgf8jHGRhx0Y9vLNzrkNQligPdRuZpHgyDEKIixMPMQow82/dC04YdgzFwdg0+2Uf1OjPzmOYhBQ6xCoYCX9626WDOo9pqNqHUO7IfBy0XxYJ8+UHdiYuJ9AHQT2GGiycHmmLNDkmFY+JCPXrlcbqcMW28/iCNpEcHnt/3SwHzhQiEIG5JAGDYsN8yHGjil5Ir9BKVDa4U5ta/xveagNDCfRBhDQ5JczEaujhHb0FlclMFzLpDTepEEgxijAL6VSCNcPLPw6aa0oSEgTZsx+GFjwyIsenRmZmbkfuQMDj8PKrjjyCHZIw02im7eGokHAQhnFjZ8GAux/+8jOhoFhX9DCIG1EsPfD9jMC5j4/rO/If4BCiyOk7IAfLMAAAAASUVORK5CYII=');vertical-align:middle;font-size:11px;color:#888;margin-right:4px;margin-top:-3px;background-position:center;height:20px;width:20px}.weapp_text_link:empty{display:none}.flex_context{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.flex_bd{-webkit-box-flex:1;-webkit-flex:1;flex:1;word-wrap:break-word;word-break:break-all}.original_page{background-color:#fff;font-size:16px}.account_info{padding:0 0 20px}.account_info .flex_bd{padding-left:.85em}.radius_avatar.account_avatar{width:28px;height:28px;padding:0}.account_nickname{overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:1;line-height:1.2;color:#576b95;font-size:14px}.account_nickname_inner{font-weight:400;vertical-align:top}.account_desc{overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:1;color:#b2b2b2;font-size:13px;line-height:1.2;padding-top:.3em}.account_desc_inner{display:inline;vertical-align:top}.share_notice{margin-bottom:16px;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto}.share_media{padding-bottom:18px}.original_panel{padding:20px;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto;overflow:hidden;position:relative}.original_panel .original_account{margin-bottom:12px;position:relative;z-index:1}.original_panel .original_account_avatar{width:28px;height:28px;padding:0}.original_panel .original_account_nickname{padding-left:.85em;font-size:15px;color:rgba(0,0,0,0.5)}.original_panel_title{font-size:17px;line-height:24px;color:rgba(0,0,0,0.9);font-weight:bold;margin:0 0 8px 0}.original_panel_content{color:#333}.original_panel_tool{padding-top:20px;position:relative;z-index:1}.appmsg_card_context{position:relative;background-color:#f7f7f7;border-radius:8px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.appmsg_card_active:active{background-color:#ebebeb}.original_area_primary{margin-bottom:24px;font-size:15px}.original_primary_tips{padding:0 16px 32px;color:rgba(0,0,0,0.5)}.original_primary_tips p:first-child{font-weight:700;padding-bottom:8px;line-height:1.4}.original_primary_card_tips{line-height:1.4;color:rgba(0,0,0,0.3)}.original_primary_card{padding:20px 16px;margin-top:16px;line-height:1.4;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.original_primary_card .radius_avatar{padding:0;width:40px;height:40px;margin-right:12px;vertical-align:middle}.original_primary_card .weui-flex__item{min-width:0}.original_primary_card .weui-flex__ft{position:relative;padding-right:24px}.original_primary_card .weui-flex__ft:after{content:"";font-size:12px;background:transparent url("data:image/svg+xml;charset=utf8, %3Csvg width='10' height='20' viewBox='0 0 10 20' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Cdefs%3E%3Cpath d='M6.323 10.358l-.884.884L.623 6.426a.83.83 0 0 1 0-1.177L5.44.433l.884.884-4.52 4.52 4.52 4.521z' id='a'/%3E%3C/defs%3E%3Cuse fill='%23000' transform='rotate(-180 4.184 7.921)' xlink:href='%23a' fill-rule='evenodd' opacity='.3' /%3E%3C/svg%3E") 0 0 no-repeat;background-size:1em;width:1em;height:2em;position:absolute;right:0;top:50%;margin-top:-1em}.original_primary_nickname{color:rgba(0,0,0,0.9);font-size:17px;font-weight:700;width:auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-wrap:normal;display:block}.original_primary_desc{color:rgba(0,0,0,0.5);font-size:14px;padding-top:4px;width:auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-wrap:normal}[class^="weui-icon-"],[class*=" weui-icon-"]{display:inline-block;vertical-align:middle;width:24px;height:24px;-webkit-mask-position:50% 50%;mask-position:50% 50%;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;-webkit-mask-size:100%;mask-size:100%;background-color:currentColor}.weui-icon-circle{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%221000%22%20height%3D%221000%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M500%20916.667C269.881%20916.667%2083.333%20730.119%2083.333%20500%2083.333%20269.881%20269.881%2083.333%20500%2083.333c230.119%200%20416.667%20186.548%20416.667%20416.667%200%20230.119-186.548%20416.667-416.667%20416.667zm0-50c202.504%200%20366.667-164.163%20366.667-366.667%200-202.504-164.163-366.667-366.667-366.667-202.504%200-366.667%20164.163-366.667%20366.667%200%20202.504%20164.163%20366.667%20366.667%20366.667z%22%20fill-rule%3D%22evenodd%22%20fill-opacity%3D%22.9%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%221000%22%20height%3D%221000%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M500%20916.667C269.881%20916.667%2083.333%20730.119%2083.333%20500%2083.333%20269.881%20269.881%2083.333%20500%2083.333c230.119%200%20416.667%20186.548%20416.667%20416.667%200%20230.119-186.548%20416.667-416.667%20416.667zm0-50c202.504%200%20366.667-164.163%20366.667-366.667%200-202.504-164.163-366.667-366.667-366.667-202.504%200-366.667%20164.163-366.667%20366.667%200%20202.504%20164.163%20366.667%20366.667%20366.667z%22%20fill-rule%3D%22evenodd%22%20fill-opacity%3D%22.9%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-download{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M11.25%2012.04l-1.72-1.72-1.06%201.06%202.828%202.83a1%201%200%20001.414-.001l2.828-2.828-1.06-1.061-1.73%201.73V7h-1.5v5.04zm0-5.04V2h1.5v5h6.251c.55%200%20.999.446.999.996v13.008a.998.998%200%2001-.996.996H4.996A.998.998%200%20014%2021.004V7.996A1%201%200%20014.999%207h6.251z%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M11.25%2012.04l-1.72-1.72-1.06%201.06%202.828%202.83a1%201%200%20001.414-.001l2.828-2.828-1.06-1.061-1.73%201.73V7h-1.5v5.04zm0-5.04V2h1.5v5h6.251c.55%200%20.999.446.999.996v13.008a.998.998%200%2001-.996.996H4.996A.998.998%200%20014%2021.004V7.996A1%201%200%20014.999%207h6.251z%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-info{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm-.75-12v7h1.5v-7h-1.5zM12%209a1%201%200%20100-2%201%201%200%20000%202z%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm-.75-12v7h1.5v-7h-1.5zM12%209a1%201%200%20100-2%201%201%200%20000%202z%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-safe-success{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201000%201000%22%3E%3Cpath%20d%3D%22M500.9%204.6C315.5%2046.7%20180.4%2093.1%2057.6%20132c0%20129.3.2%20231.7.2%20339.7%200%20304.2%20248.3%20471.6%20443.1%20523.7C695.7%20943.3%20944%20775.9%20944%20471.7c0-108%20.2-210.4.2-339.7C821.4%2093.1%20686.3%2046.7%20500.9%204.6zm248.3%20349.1l-299.7%20295c-2.1%202-5.3%202-7.4-.1L304.4%20506.1c-2-2.1-2.3-5.7-.6-8l18.3-24.9c1.7-2.3%205-2.8%207.2-1l112.2%2086c2.3%201.8%206%201.7%208.1-.1l274.7-228.9c2.2-1.8%205.7-1.7%207.7.3l17%2016.8c2.2%202.1%202.2%205.3.2%207.4z%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20fill%3D%22%23070202%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201000%201000%22%3E%3Cpath%20d%3D%22M500.9%204.6C315.5%2046.7%20180.4%2093.1%2057.6%20132c0%20129.3.2%20231.7.2%20339.7%200%20304.2%20248.3%20471.6%20443.1%20523.7C695.7%20943.3%20944%20775.9%20944%20471.7c0-108%20.2-210.4.2-339.7C821.4%2093.1%20686.3%2046.7%20500.9%204.6zm248.3%20349.1l-299.7%20295c-2.1%202-5.3%202-7.4-.1L304.4%20506.1c-2-2.1-2.3-5.7-.6-8l18.3-24.9c1.7-2.3%205-2.8%207.2-1l112.2%2086c2.3%201.8%206%201.7%208.1-.1l274.7-228.9c2.2-1.8%205.7-1.7%207.7.3l17%2016.8c2.2%202.1%202.2%205.3.2%207.4z%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20fill%3D%22%23070202%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-safe-warn{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201000%201000%22%3E%3Cpath%20d%3D%22M500.9%204.5c-185.4%2042-320.4%2088.4-443.2%20127.3%200%20129.3.2%20231.7.2%20339.6%200%20304.1%20248.2%20471.4%20443%20523.6%20194.7-52.2%20443-219.5%20443-523.6%200-107.9.2-210.3.2-339.6C821.3%2092.9%20686.2%2046.5%20500.9%204.5zm-26.1%20271.1h52.1c5.8%200%2010.3%204.7%2010.1%2010.4l-11.6%20313.8c-.1%202.8-2.5%205.2-5.4%205.2h-38.2c-2.9%200-5.3-2.3-5.4-5.2L464.8%20286c-.2-5.8%204.3-10.4%2010-10.4zm26.1%20448.3c-20.2%200-36.5-16.3-36.5-36.5s16.3-36.5%2036.5-36.5%2036.5%2016.3%2036.5%2036.5-16.4%2036.5-36.5%2036.5z%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20fill%3D%22%23020202%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201000%201000%22%3E%3Cpath%20d%3D%22M500.9%204.5c-185.4%2042-320.4%2088.4-443.2%20127.3%200%20129.3.2%20231.7.2%20339.6%200%20304.1%20248.2%20471.4%20443%20523.6%20194.7-52.2%20443-219.5%20443-523.6%200-107.9.2-210.3.2-339.6C821.3%2092.9%20686.2%2046.5%20500.9%204.5zm-26.1%20271.1h52.1c5.8%200%2010.3%204.7%2010.1%2010.4l-11.6%20313.8c-.1%202.8-2.5%205.2-5.4%205.2h-38.2c-2.9%200-5.3-2.3-5.4-5.2L464.8%20286c-.2-5.8%204.3-10.4%2010-10.4zm26.1%20448.3c-20.2%200-36.5-16.3-36.5-36.5s16.3-36.5%2036.5-36.5%2036.5%2016.3%2036.5%2036.5-16.4%2036.5-36.5%2036.5z%22%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20fill%3D%22%23020202%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-success{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm-1.177-7.86l-2.765-2.767L7%2012.431l3.119%203.121a1%201%200%20001.414%200l5.952-5.95-1.062-1.062-5.6%205.6z%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm-1.177-7.86l-2.765-2.767L7%2012.431l3.119%203.121a1%201%200%20001.414%200l5.952-5.95-1.062-1.062-5.6%205.6z%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-success-circle{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm0-1.2a8.8%208.8%200%20100-17.6%208.8%208.8%200%20000%2017.6zm-1.172-6.242l5.809-5.808.848.849-5.95%205.95a1%201%200%2001-1.414%200L7%2012.426l.849-.849%202.98%202.98z%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm0-1.2a8.8%208.8%200%20100-17.6%208.8%208.8%200%20000%2017.6zm-1.172-6.242l5.809-5.808.848.849-5.95%205.95a1%201%200%2001-1.414%200L7%2012.426l.849-.849%202.98%202.98z%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-success-no-circle{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M8.657%2018.435L3%2012.778l1.414-1.414%204.95%204.95L20.678%205l1.414%201.414-12.02%2012.021a1%201%200%2001-1.415%200z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M8.657%2018.435L3%2012.778l1.414-1.414%204.95%204.95L20.678%205l1.414%201.414-12.02%2012.021a1%201%200%2001-1.415%200z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-waiting{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12.75%2011.38V6h-1.5v6l4.243%204.243%201.06-1.06-3.803-3.804zM12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12.75%2011.38V6h-1.5v6l4.243%204.243%201.06-1.06-3.803-3.804zM12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-waiting-circle{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12.6%2011.503l3.891%203.891-.848.849L11.4%2012V6h1.2v5.503zM12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm0-1.2a8.8%208.8%200%20100-17.6%208.8%208.8%200%20000%2017.6z%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12.6%2011.503l3.891%203.891-.848.849L11.4%2012V6h1.2v5.503zM12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm0-1.2a8.8%208.8%200%20100-17.6%208.8%208.8%200%20000%2017.6z%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-warn{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm-.763-15.864l.11%207.596h1.305l.11-7.596h-1.525zm.759%2010.967c.512%200%20.902-.383.902-.882%200-.5-.39-.882-.902-.882a.878.878%200%2000-.896.882c0%20.499.396.882.896.882z%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm-.763-15.864l.11%207.596h1.305l.11-7.596h-1.525zm.759%2010.967c.512%200%20.902-.383.902-.882%200-.5-.39-.882-.902-.882a.878.878%200%2000-.896.882c0%20.499.396.882.896.882z%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-info-circle{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm0-1.2a8.8%208.8%200%20100-17.6%208.8%208.8%200%20000%2017.6zM11.4%2010h1.2v7h-1.2v-7zm.6-1a1%201%200%20110-2%201%201%200%20010%202z%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm0-1.2a8.8%208.8%200%20100-17.6%208.8%208.8%200%20000%2017.6zM11.4%2010h1.2v7h-1.2v-7zm.6-1a1%201%200%20110-2%201%201%200%20010%202z%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-cancel{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cg%20fill-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm0-1.2a8.8%208.8%200%20100-17.6%208.8%208.8%200%20000%2017.6z%22%20fill-rule%3D%22nonzero%22%2F%3E%3Cpath%20d%3D%22M12.849%2012l3.11%203.111-.848.849L12%2012.849l-3.111%203.11-.849-.848L11.151%2012l-3.11-3.111.848-.849L12%2011.151l3.111-3.11.849.848L12.849%2012z%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cg%20fill-rule%3D%22evenodd%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm0-1.2a8.8%208.8%200%20100-17.6%208.8%208.8%200%20000%2017.6z%22%20fill-rule%3D%22nonzero%22%2F%3E%3Cpath%20d%3D%22M12.849%2012l3.11%203.111-.848.849L12%2012.849l-3.111%203.11-.849-.848L11.151%2012l-3.11-3.111.848-.849L12%2011.151l3.111-3.11.849.848L12.849%2012z%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E)}.weui-icon-search{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M16.31%2015.561l4.114%204.115-.848.848-4.123-4.123a7%207%200%2011.857-.84zM16.8%2011a5.8%205.8%200%2010-11.6%200%205.8%205.8%200%200011.6%200z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M16.31%2015.561l4.114%204.115-.848.848-4.123-4.123a7%207%200%2011.857-.84zM16.8%2011a5.8%205.8%200%2010-11.6%200%205.8%205.8%200%200011.6%200z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-clear{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M13.06%2012l3.006-3.005-1.06-1.06L12%2010.938%208.995%207.934l-1.06%201.06L10.938%2012l-3.005%203.005%201.06%201.06L12%2013.062l3.005%203.005%201.06-1.06L13.062%2012zM12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010z%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M13.06%2012l3.006-3.005-1.06-1.06L12%2010.938%208.995%207.934l-1.06%201.06L10.938%2012l-3.005%203.005%201.06%201.06L12%2013.062l3.005%203.005%201.06-1.06L13.062%2012zM12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010z%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-back{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm1.999-6.563L10.68%2012%2014%208.562%2012.953%207.5%209.29%2011.277a1.045%201.045%200%20000%201.446l3.663%203.777L14%2015.437z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm1.999-6.563L10.68%2012%2014%208.562%2012.953%207.5%209.29%2011.277a1.045%201.045%200%20000%201.446l3.663%203.777L14%2015.437z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-delete{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M6.774%206.4l.812%2013.648a.8.8%200%2000.798.752h7.232a.8.8%200%2000.798-.752L17.226%206.4H6.774zm11.655%200l-.817%2013.719A2%202%200%200115.616%2022H8.384a2%202%200%2001-1.996-1.881L5.571%206.4H3.5v-.7a.5.5%200%2001.5-.5h16a.5.5%200%2001.5.5v.7h-2.071zM14%203a.5.5%200%2001.5.5v.7h-5v-.7A.5.5%200%200110%203h4zM9.5%209h1.2l.5%209H10l-.5-9zm3.8%200h1.2l-.5%209h-1.2l.5-9z%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M6.774%206.4l.812%2013.648a.8.8%200%2000.798.752h7.232a.8.8%200%2000.798-.752L17.226%206.4H6.774zm11.655%200l-.817%2013.719A2%202%200%200115.616%2022H8.384a2%202%200%2001-1.996-1.881L5.571%206.4H3.5v-.7a.5.5%200%2001.5-.5h16a.5.5%200%2001.5.5v.7h-2.071zM14%203a.5.5%200%2001.5.5v.7h-5v-.7A.5.5%200%200110%203h4zM9.5%209h1.2l.5%209H10l-.5-9zm3.8%200h1.2l-.5%209h-1.2l.5-9z%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-success-no-circle-thin{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M8.864%2016.617l-5.303-5.303-1.061%201.06%205.657%205.657a1%201%200%20001.414%200L21.238%206.364l-1.06-1.06L8.864%2016.616z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M8.864%2016.617l-5.303-5.303-1.061%201.06%205.657%205.657a1%201%200%20001.414%200L21.238%206.364l-1.06-1.06L8.864%2016.616z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-arrow{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2212%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M2.454%206.58l1.06-1.06%205.78%205.779a.996.996%200%20010%201.413l-5.78%205.779-1.06-1.061%205.425-5.425-5.425-5.424z%22%20fill%3D%22%23B2B2B2%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2212%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M2.454%206.58l1.06-1.06%205.78%205.779a.996.996%200%20010%201.413l-5.78%205.779-1.06-1.061%205.425-5.425-5.425-5.424z%22%20fill%3D%22%23B2B2B2%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-arrow-bold{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20height%3D%2224%22%20width%3D%2212%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M10.157%2012.711L4.5%2018.368l-1.414-1.414%204.95-4.95-4.95-4.95L4.5%205.64l5.657%205.657a1%201%200%20010%201.414z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20height%3D%2224%22%20width%3D%2212%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M10.157%2012.711L4.5%2018.368l-1.414-1.414%204.95-4.95-4.95-4.95L4.5%205.64l5.657%205.657a1%201%200%20010%201.414z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-back-arrow{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2212%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M3.343%2012l7.071%207.071L9%2020.485l-7.778-7.778a1%201%200%20010-1.414L9%203.515l1.414%201.414L3.344%2012z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2212%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M3.343%2012l7.071%207.071L9%2020.485l-7.778-7.778a1%201%200%20010-1.414L9%203.515l1.414%201.414L3.344%2012z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-back-arrow-thin{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2212%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M10%2019.438L8.955%2020.5l-7.666-7.79a1.02%201.02%200%20010-1.42L8.955%203.5%2010%204.563%202.682%2012%2010%2019.438z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2212%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M10%2019.438L8.955%2020.5l-7.666-7.79a1.02%201.02%200%20010-1.42L8.955%203.5%2010%204.563%202.682%2012%2010%2019.438z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-close{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2010.586l5.657-5.657%201.414%201.414L13.414%2012l5.657%205.657-1.414%201.414L12%2013.414l-5.657%205.657-1.414-1.414L10.586%2012%204.929%206.343%206.343%204.93%2012%2010.586z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2010.586l5.657-5.657%201.414%201.414L13.414%2012l5.657%205.657-1.414%201.414L12%2013.414l-5.657%205.657-1.414-1.414L10.586%2012%204.929%206.343%206.343%204.93%2012%2010.586z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-close-thin{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12.25%2010.693L6.057%204.5%205%205.557l6.193%206.193L5%2017.943%206.057%2019l6.193-6.193L18.443%2019l1.057-1.057-6.193-6.193L19.5%205.557%2018.443%204.5z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12.25%2010.693L6.057%204.5%205%205.557l6.193%206.193L5%2017.943%206.057%2019l6.193-6.193L18.443%2019l1.057-1.057-6.193-6.193L19.5%205.557%2018.443%204.5z%22%20fill-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-back-circle{-webkit-mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm0-1.2a8.8%208.8%200%20100-17.6%208.8%208.8%200%20000%2017.6zm1.999-5.363L12.953%2016.5%209.29%2012.723a1.045%201.045%200%20010-1.446L12.953%207.5%2014%208.563%2010.68%2012%2014%2015.438z%22%2F%3E%3C%2Fsvg%3E);mask-image:url(data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M12%2022C6.477%2022%202%2017.523%202%2012S6.477%202%2012%202s10%204.477%2010%2010-4.477%2010-10%2010zm0-1.2a8.8%208.8%200%20100-17.6%208.8%208.8%200%20000%2017.6zm1.999-5.363L12.953%2016.5%209.29%2012.723a1.045%201.045%200%20010-1.446L12.953%207.5%2014%208.563%2010.68%2012%2014%2015.438z%22%2F%3E%3C%2Fsvg%3E)}.weui-icon-success{color:#07c160}.weui-icon-waiting{color:#10aeff}.weui-icon-warn{color:#fa5151}.weui-icon-info{color:#10aeff}.weui-icon-success-circle{color:#07c160}.weui-icon-success-no-circle,.weui-icon-success-no-circle-thin{color:#07c160}.weui-icon-waiting-circle{color:#10aeff}.weui-icon-circle{color:rgba(0,0,0,0.3)}.weui-icon-download{color:#07c160}.weui-icon-info-circle{color:rgba(0,0,0,0.3)}.weui-icon-safe-success{color:#07c160}.weui-icon-safe-warn{color:#ffbe00}.weui-icon-cancel{color:#fa5151}.weui-icon-search{color:rgba(0,0,0,0.5)}.weui-icon-clear{color:rgba(0,0,0,0.3)}.weui-icon-clear:active{color:rgba(0,0,0,0.5)}.weui-icon-delete.weui-icon_gallery-delete{color:#fff}.weui-icon-arrow,.weui-icon-arrow-bold,.weui-icon-back-arrow,.weui-icon-back-arrow-thin{width:12px}.weui-icon-arrow,.weui-icon-arrow-bold{color:rgba(0,0,0,0.3)}.weui-icon-back-arrow,.weui-icon-back-arrow-thin{color:rgba(0,0,0,0.9)}.weui-icon-back,.weui-icon-back-circle{color:rgba(0,0,0,0.9)}.weui-icon_msg{width:64px;height:64px}.weui-icon_msg.weui-icon-warn{color:#fa5151}.weui-icon_msg-primary{width:64px;height:64px}.weui-icon_msg-primary.weui-icon-warn{color:#ffc300}.weui-textarea{-webkit-tap-highlight-color:rgba(0,0,0,0);background-color:transparent;display:block;border:0;resize:none;width:100%;color:inherit;font-size:1em;line-height:inherit;outline:0}.weui-flex{display:-webkit-box;display:-webkit-flex;display:flex}.weui-flex__item{-webkit-box-flex:1;-webkit-flex:1;flex:1}.weui-media-box{padding:16px;position:relative}.weui-media-box:before{content:" ";position:absolute;left:0;top:0;right:0;height:1px;border-top:1px solid rgba(0,0,0,0.1);-webkit-transform-origin:0 0;transform-origin:0 0;-webkit-transform:scaleY(0.5);transform:scaleY(0.5);left:16px}.weui-media-box:first-child:before{display:none}a.weui-media-box{color:#000;-webkit-tap-highlight-color:rgba(0,0,0,0)}a.weui-media-box:active{background-color:#ececec}.weui-media-box__title{font-weight:400;font-size:17px;line-height:1.4;color:rgba(0,0,0,0.9);width:auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-wrap:normal;word-wrap:break-word;word-break:break-all}.weui-media-box__desc{color:rgba(0,0,0,0.3);font-size:14px;line-height:1.4;padding-top:4px;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:2}.weui-media-box__info{margin-top:16px;padding-bottom:4px;font-size:13px;color:#cecece;line-height:1em;list-style:none;overflow:hidden}.weui-media-box__info__meta{float:left;padding-right:1em}.weui-media-box__info__meta_extra{padding-left:1em;border-left:1px solid #cecece}.weui-media-box_appmsg{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.weui-media-box_appmsg .weui-media-box__hd{margin-right:16px;width:60px;height:60px;line-height:60px;text-align:center}.weui-media-box_appmsg .weui-media-box__thumb{width:100%;max-height:100%;vertical-align:top}.weui-media-box_appmsg .weui-media-box__bd{-webkit-box-flex:1;-webkit-flex:1;flex:1;min-width:0}.weui-media-box_small-appmsg{padding:0}.weui-media-box_small-appmsg .weui-cells{margin-top:0}.weui-media-box_small-appmsg .weui-cells:before{display:none}.weui-btn{position:relative;display:block;width:184px;margin-left:auto;margin-right:auto;padding:8px 24px;box-sizing:border-box;font-weight:700;font-size:17px;text-align:center;text-decoration:none;color:#fff;line-height:1.41176471;border-radius:4px;-webkit-tap-highlight-color:rgba(0,0,0,0);overflow:hidden}.weui-btn_block{width:auto}.weui-btn_inline{display:inline-block}.weui-btn_default{color:#06ae56;background-color:#f2f2f2}.weui-btn_default:not(.weui-btn_disabled):visited{color:#06ae56}.weui-btn_default:not(.weui-btn_disabled):active{color:#06ae56;background-color:#d9d9d9}.weui-btn_primary{background-color:#07c160}.weui-btn_primary:not(.weui-btn_disabled):visited{color:#fff}.weui-btn_primary:not(.weui-btn_disabled):active{color:#fff;background-color:#06ad56}.weui-btn_warn{color:#fa5151;background-color:#f2f2f2}.weui-btn_warn:not(.weui-btn_disabled):visited{color:#fa5151}.weui-btn_warn:not(.weui-btn_disabled):active{color:#fa5151;background-color:#d9d9d9}.weui-btn_disabled{color:rgba(0,0,0,0.18);background-color:#fafafa}.weui-btn_loading .weui-loading{margin:-0.2em .34em 0 0}.weui-btn_loading.weui-btn_primary{color:#fff}.weui-btn_loading.weui-btn_default{background-color:#d9d9d9}.weui-btn_loading.weui-btn_primary{background-color:#06ad56}.weui-btn_loading.weui-btn_warn{background-color:#d9d9d9}.weui-btn_plain-primary{color:#07c160;border:1px solid #1aad19}.weui-btn_plain-primary:not(.weui-btn_plain-disabled):active{color:#06ae56;border-color:#179c16;background-color:rgba(0,0,0,0.1)}.weui-btn_plain-primary:after{border-width:0}.weui-btn_plain-default{color:#353535;border:1px solid #353535}.weui-btn_plain-default:not(.weui-btn_plain-disabled):active{color:#323232;border-color:#323232;background-color:rgba(0,0,0,0.1)}.weui-btn_plain-default:after{border-width:0}.weui-btn_plain-disabled{color:rgba(0,0,0,0.2);border-color:rgba(0,0,0,0.2)}.weui-btn_cell{position:relative;display:block;margin-left:auto;margin-right:auto;box-sizing:border-box;font-weight:700;font-size:17px;text-align:center;text-decoration:none;color:#fff;line-height:1.41176471;padding:16px;-webkit-tap-highlight-color:rgba(0,0,0,0);overflow:hidden;background-color:#fff}.weui-btn_cell+.weui-btn_cell{margin-top:16px}.weui-btn_cell:active{background-color:#ececec}.weui-btn_cell__icon{display:inline-block;vertical-align:middle;width:24px;height:24px;margin:-0.2em .34em 0 0}.weui-btn_cell-default{color:rgba(0,0,0,0.9)}.weui-btn_cell-primary{color:#576b95}.weui-btn_cell-warn{color:#fa5151}button.weui-btn,input.weui-btn{border-width:0;outline:0;-webkit-appearance:none}button.weui-btn:focus,input.weui-btn:focus{outline:0}button.weui-btn_inline,input.weui-btn_inline,button.weui-btn_mini,input.weui-btn_mini{width:auto}button.weui-btn_plain-primary,input.weui-btn_plain-primary,button.weui-btn_plain-default,input.weui-btn_plain-default{border-width:1px;background-color:transparent}.weui-btn_mini{display:inline-block;width:auto;padding:0 .75em;line-height:2;font-size:16px}.weui-btn:not(.weui-btn_mini)+.weui-btn:not(.weui-btn_mini){margin-top:16px}.weui-btn.weui-btn_inline+.weui-btn.weui-btn_inline{margin-top:auto;margin-left:16px}.weui-btn-area{margin:48px 16px 8px}.weui-btn-area_inline{display:-webkit-box;display:-webkit-flex;display:flex}.weui-btn-area_inline .weui-btn{margin-top:auto;margin-right:16px;width:100%;-webkit-box-flex:1;-webkit-flex:1;flex:1}.weui-btn-area_inline .weui-btn:last-child{margin-right:0}.weui-btn_reset{background:transparent;border:0;padding:0;outline:0}.weui-btn_icon{font-size:0}.weui-btn_icon:active [class*="weui-icon-"]{color:rgba(0,0,0,0.5)}.preview_appmsg .rich_media_title{margin-top:1.5em}.preview_appmsg .account_info{padding-top:3em}.original_page{background-color:transparent}.account_info{-webkit-tap-highlight-color:rgba(0,0,0,0);outline:0;padding-bottom:16px;font-size:16px}.account_info.appmsg_account_info{padding-bottom:32px}.account_info .radius_avatar img{background-color:transparent}.share_notice{font-size:17px;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto}.original_panel .original_account_avatar{width:30px;height:30px}.original_panel_tool{font-size:14px}.original_panel_tool a{color:#576b95}.original_panel_content{opacity:.90;font-size:14px;line-height:22px;color:#000}.share_media{padding-bottom:30px}.icon_appmsg_tag{display:inline-block;vertical-align:middle;padding:0 .5em;font-size:12px;line-height:1.67;background-color:#c3c3c3;color:#fff;border-radius:2px;-moz-border-radius:2px;-webkit-border-radius:2px;width:auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-wrap:normal;max-width:70%}.icon_appmsg_tag.primary{color:#3bb638;padding:4px .78em;background-color:rgba(9,187,7,0.08);font-size:12px;border-top-left-radius:.95em 50%;-moz-border-radius-topleft:.95em 50%;-webkit-border-top-left-radius:.95em 50%;border-top-right-radius:.95em 50%;-moz-border-radius-topright:.95em 50%;-webkit-border-top-right-radius:.95em 50%;border-bottom-left-radius:.95em 50%;-moz-border-radius-bottomleft:.95em 50%;-webkit-border-bottom-left-radius:.95em 50%;border-bottom-right-radius:.95em 50%;-moz-border-radius-bottomright:.95em 50%;-webkit-border-bottom-right-radius:.95em 50%}.icon_appmsg_tag.default{border:1px solid rgba(0,0,0,0.1);color:rgba(0,0,0,0.3);background-color:transparent;padding:0 .54em;font-size:15px;line-height:1.3;border-top-left-radius:.67em 50%;-moz-border-radius-topleft:.67em 50%;-webkit-border-top-left-radius:.67em 50%;border-top-right-radius:.67em 50%;-moz-border-radius-topright:.67em 50%;-webkit-border-top-right-radius:.67em 50%;border-bottom-left-radius:.67em 50%;-moz-border-radius-bottomleft:.67em 50%;-webkit-border-bottom-left-radius:.67em 50%;border-bottom-right-radius:.67em 50%;-moz-border-radius-bottomright:.67em 50%;-webkit-border-bottom-right-radius:.67em 50%}.rich_media_meta_list .icon_appmsg_tag.default{margin-top:-1px}.icon_appmsg_tag.title_tag{background-color:#d04b4e}.icon_appmsg_tag.appmsg_title_tag{background:#f2f2f2;color:rgba(0,0,0,0.3);padding:0 4px}.icon_global_tag_wrp{text-align:right;padding-bottom:12px}.icon_global_tag{background-color:rgba(118,118,118,0.16);color:rgba(0,0,0,0.41);line-height:2.2;border-top-left-radius:1em 50%;-moz-border-radius-topleft:1em 50%;-webkit-border-top-left-radius:1em 50%;border-bottom-left-radius:1em 50%;-moz-border-radius-bottomleft:1em 50%;-webkit-border-bottom-left-radius:1em 50%;padding:0 1.8em 0 1.34em;font-size:12px;margin-right:-24px;display:inline-block;vertical-align:top}.global_plain_btn{display:inline-block;vertical-align:middle;padding:0 1em;line-height:2;font-size:14px;-webkit-tap-highlight-color:rgba(0,0,0,0);border-radius:5px;-moz-border-radius:5px;-webkit-border-radius:5px}.global_plain_btn.primary{color:#1aad19;border:1px solid currentColor}.global_plain_btn.primary:active{color:rgba(26,173,25,0.6)}.wx_video_context{color:#fefefe;position:relative;background-color:#000}.wx_video_thumb,.wx_video_thumb_primary{position:absolute;left:0;width:100%;height:100%!important;top:0}.wx_video_thumb_primary{background-size:cover;background-position:50% 50%;background-repeat:no-repeat}.wx_video_play_btn{position:absolute;left:50%;top:50%;-webkit-transform:translate(-50%,-50%);transform:translate(-50%,-50%);font-size:0;border-width:0;background-color:transparent;padding:0;outline:0;z-index:2;width:48px;height:48px;background:rgba(237,237,237,0.9);border-radius:50%;text-align:center}.wx_video_play_btn:before{content:"";display:inline-block;width:28px;height:28px;vertical-align:middle;background-size:cover;background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cpath fill='%23151515' fill-rule='evenodd' d='M9.524 4.938l10.092 6.21a1 1 0 0 1 0 1.704l-10.092 6.21A1 1 0 0 1 8 18.21V5.79a1 1 0 0 1 1.524-.852z'/%3E%3C/svg%3E")}.wx_video_mask{position:absolute;top:0;left:0;right:0;bottom:0;z-index:1;background-color:rgba(0,0,0,0.5)}.wx_video_loading{position:absolute;left:50%;top:50%;margin-top:-20px;margin-left:-20px;width:40px;height:40px;z-index:2;background:transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAEH0lEQVR42uXb2U9UZxzG8d+wzCKLQylLEbUIopVNBUGoIIuIVkWbWtDGlLZWoWrRqtRq3bvbpvtFL/qH9Lo3TXrfv6Hpbf8B+p3kOcmbN0Nimw4w532STw7xAuZ5wsyccwat0FleXq5ED45iDu/jMX7F3/gTty1OoVAzprGEb/AtvsP3+BG/wM+MFXMokMIIbuIJvgI0gEbQAH/Az89WjOGBZ3AI9/E5vniKAX6DnztWTOEBJ7AXH+JTfBYNIF/K197T4Af8hL8Q5XdUWrGEB5vFBXyET0QDIP8AH+MKZjGJMcxhFGVWLOHBbsESHgkjQL8FzhBPsIADaLQ4hCJ7cA8PAW8A6N8mkbW4hDIlOIy7uI8H8hCPHdNF9Vz+F+VfVXkNAA2AR5hFrcUxeou7jTtyVx7gHnZbXKNT2Fv4IM8AN7DZ4hqdzt6EBgA0wnlstLiGctW4jCXckmiIt5C0uEZneGdwQ5acIRZRbXEOBTtx3R9AX2+yOIeCaczjGt6T69JpcQ8l9+MqrkVHlT9ucQ8lk7iYZ4DFWJ3WrhRd2r6LRbkqYxZCKHoWl3BZrmAeGyzuoWSdyvsDDFgIoegQFuQduYQqCyG62pvHgnOcthCim5oXMO9YCOJ9XwO0aICLnhoLIbrNdd7xNs5ZKNHdWX+AYxZKKHsCb+BNx5CFEsqe1gBzuaN0WSjRtf+cZ6eFktwLHl73bLNQQtnXcM7TYqGEsjN5Bmi3UKJPc856dlkooewUznj6LJRQdhCzKj6bE8xNEA3QodIzjpMWSvQJ0GnHKzmxv//vDJBaYYA2CyX6BPhlzwELJZTtxinHSR0zFkIomnWL6zgd2jXBeFRcTuAlpCyEULRVpY/LMemwEELRMhzJM8AUKiyEULQdR+VIJNZ/B+QNUI4JTKn4lKPJQghFm70BJmU8lE+JExjAYZmUCQwjbXGPPi06iEMYlzHpQ6nFPTo5msC4jOKgjr3r6fwg91tbqG/chFGJBhjBMPrXwxWjnrJlKMkpxA9oU/HIsLyIIdSvYflSlBV6gAQ6MRIVl0HZj+2r+eKoskmkkJRSSeQUYoRt7gAqPuAce7EV5QUunkIF0khJwQbwH0CDCg86xfuxD73SjUYk/+fiGWxEpWxAxhmiXEpW4++I+5wB9jkD7MVu9GiIVtQi9R+vTTKoxjPIaoAqaABoACRRspq30TrQjz7ZI+4AXdgl27EZ9ahRsUqpkqzK1ksdav0BpELSKp9Yi7efOhXui8pLD7qcAV7ATuxAm7TgeWzFFmySRjR4A0ADMJw3QBkSa30Z3aSyPdKNTnHLtz/FAM95I9RKjTdCCglbL9ErcL2KFmSAdVl8pWsJlWiLyjsDtIo/QLP4A9Sgsqj+c2Wep0gVnlW5ZpWGBlBxNDiF06vxqv4PFQWElSE4GpoAAAAASUVORK5CYII=) 0 0 no-repeat;background-size:100%;-webkit-animation:loading 1000ms steps(60,end) 0ms infinite;animation:loading 1000ms steps(60,end) 0ms infinite}@-webkit-keyframes loading{0%{-webkit-transform:rotate3d(0,0,1,0deg)}100%{-webkit-transform:rotate3d(0,0,1,360deg)}}@keyframes loading{0%{-webkit-transform:rotate3d(0,0,1,0deg)}100%{-webkit-transform:rotate3d(0,0,1,360deg)}}.place_audio_area{min-height:100px;background-color:#fdfdfd;display:block;margin:16px 0}.place_music_area{min-height:68px;background-color:#fdfdfd;display:block;margin:17px 0 16px}.rich_media_empty_extra{background-color:#fafafa}.appmsg_skin_default.rich_media_empty_extra{background-color:#fff}.appmsg_skin_default .rich_media_area_primary{background-color:#fff}.appmsg_skin_default .rich_media_area_primary .weui-loadmore_line .weui-loadmore__tips{background-color:#fff}.appmsg_style_default .rich_media_tool{padding-top:15px}.rich_media_title_ios{font-weight:700}.my_comment_empty_data{background-color:#fff}.read-more__area{margin:30px 0}.read-more__desc{margin-bottom:10px}.read-more__article__extra{font-size:14px;color:rgba(0,0,0,0.5)}.read-more__article__item{margin-bottom:10px}.original_panel_tips{font-size:12px;color:#fff;line-height:20px;font-weight:normal;vertical-align:2px;padding:0 4px;border-radius:2px;display:inline-block;background-color:rgba(0,0,0,0.2)}.original_panel_tips2{font-size:12px;color:rgba(0,0,0,0.3);line-height:20px;font-weight:normal;vertical-align:2px;padding:0 4px;border-radius:2px;display:inline-block;background-color:rgba(0,0,0,0.05)}@font-face{font-family:"WeChatSansStd-Medium";src:url(data:application/x-font-ttf;charset=utf-8;base64,AAEAAAAKAIAAAwAgT1MvMmsyak0AAACsAAAAYGNtYXAVQx11AAABDAAAAWJnbHlmfLj7WQAAAnAAAARAaGVhZA/uXt4AAAawAAAANmhoZWEFsgG+AAAG6AAAACRobXR4G1wCswAABwwAAAA2bG9jYQfwBtgAAAdEAAAAHm1heHAAEgA2AAAHZAAAACBuYW1lNeaNfgAAB4QAAAUtcG9zdLTpTnoAAAy0AAAARgAEAhsB9AAFAAgCigJYAAAASwKKAlgAAAFeADIBMAAAAAAGAAAAAAAAAAAAAAEQAAAAAAAAAAAAAABITllJAAAAJP/lA4T/MwAAA4QAzQAAAQAAAAAAAfsCyAAAACAAAgAAAAMAAAADAAAAHAABAAAAAABcAAMAAQAAABwABABAAAAADAAIAAIABAAkAC4AOf/l/////wAAACQALgAw/+X//////+j/3f/RACgAAQABAAAAAAAAAAAAAAAAAAABBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAsAAQIDBAUGBwgJCgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIASAAAAhACyAADAAcAABMhESElESERSAHI/jgBdP7gAsj9OE0CLv3SAAAAAgBA//IB9QLWAA0AFwAAFiY9ATQ2MzIWHQEUBiM2PQE0IyIdARQzrm5ubWxubmxtbW1tDpqYhJaYmJaEmJpoxozCwozGAAAAAQALAAABOgLIAAYAABMHJzczESPMhTzKZW4CO2NWmv04AAAAAQA9AAAB/ALWABkAADcTPgE1NCYjIgYHJz4BMzIeARUUBg8BIRUhPfYwJjotK0cYWiJ2UTpfNzI+sgEn/kFTARE2USUpND02MVBbMlg3Nm9Ex2UAAQA4//ICBQLIAB0AADceATMyNjU0JiMiBzU3IzUhFQc2HgEVFA4BIyImJ4wZRyk5SU9GKSWb/QGLqz1gNjxrRUZ1Jq0nK0c1PDwIW71pWMcDMWBDQmk7QjwAAAACABgAAAIQAsgACgANAAAlITUBMxEzFSMVIzURAwFP/skBLXdUVG3CmUQB6/4oV5nwAUD+wAAAAAEAMf/yAgQCyAAeAAAWJic3HgEzMjY1NCYjIgcjESEVIRU2MzIeARUUDgEjz3klWRNLKjtMSThBL1EBgP7tLkU7XTU8bEUOSUI1KTJMPDlKNQGbZL8fOWdCRm09AAAAAAIANf/yAgUCyAATAB8AABYuATU0NjcTMwM2MzIeARUUDgEjPgE1NCYjIgYVFBYz3Go9HSepdaUcIj1hNzxqQTRGRjQ1RkY1DjxoQCVQRQE4/tsROWY/QGg8Y0k3N0pJODdJAAABACYAAAHUAsgABgAAASE1IRUDIwFc/soBrulzAmRkVf2NAAADAC//8gIHAtYAGwAnADMAABYuATU0NjcuATU0PgEzMh4BFRQGBx4BFRQOASMSNjU0JiMiBhUUFjMSNjU0JiMiBhUUFjPYaz5GNC04OGI9PGE4OCw1Rj5sQi48PS0vPT0vNkhJNTZJSDcONl87RmIUFkw1NlgzM1g2NUsXFmFFO182Abo5LSs3NystOf6oRDQ2SUk2NEQAAAIANQAAAgUC1gATAB8AAAEGIyIuATU0PgEzMh4BFRQGBwMjEjY1NCYjIgYVFBYzAUgcIj1hNzxqQkFqPR0mqnWvRkY1NUVGNAElETlmP0BoPDxoQCRQRv7IAXJJODdJSTc4SQABAFMAAADBAG0AAwAANzUzFVNuAG1tAAABAFD/twIJAwYAKQAAJAYHFSM1Jic3HgEzMjY1NCYnLgE1NDY3NTMVFhcHLgEjIgYVFBYXHgEVAglVSG1nSEYcSio0QDk7ZmNZSW1WPEcfPiMvPjg7aWOCZBFWUQ1KSh0hMCgkMBIeX0tMZQ1XWBRJQyIgMSgkLxIeX0oAAQAzAAACIQK6ABYAAAEzFSMVMxUjFSM1IzUzNSM1MwMzGwEzAX12k5OTbZOTk3ajdYKCdQFZUjlSfHxSOVIBYf7MATQAAAAAAQAAAAEAAGOe0lxfDzz1AAMD6AAAAADVtvhtAAAAANj0ItAAC/+3AiEDBgAAAAcAAgAAAAAAAAABAAADhP8zAAACWAALACUCIQABAAAAAAAAAAAAAAAAAAAADQJYAEgCNQBAAboACwI1AD0CNQA4AjUAGAI1ADECNQA1AgEAJgI1AC8CNQA1ARYAUwJYAFAAMwAAAAAAFgA6AEwAdgCkAMAA8AEiATQBgAGyAb4B/AIgAAAAAQAAAA4ANAADAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAABwBVgABAAAAAAAAADMAAAABAAAAAAABABYAMwABAAAAAAACAAcASQABAAAAAAADACoAUAABAAAAAAAEABYAegABAAAAAAAFAAwAkAABAAAAAAAGABYAnAABAAAAAAAHACYAsgABAAAAAAAIAAsA2AABAAAAAAAJACMA4wABAAAAAAALABgBBgABAAAAAAAQAA8BHgABAAAAAAARAAYBLQABAAAAAAATABgBMwADAAEECQAAAGYBSwADAAEECQABACwBsQADAAEECQACAA4B3QADAAEECQADAFQB6wADAAEECQAEACwCPwADAAEECQAFABgCawADAAEECQAGACwCgwADAAEECQAHAEwCrwADAAEECQAIABYC+wADAAEECQAJAEYDEQADAAEECQALADADVwADAAEECQAQAB4DhwADAAEECQARAAwDpQADAAEECQATACYDsUNvcHlyaWdodCAoYykgMjAxNyBieSBUZW5jZW50LiBBbGwgcmlnaHRzIHJlc2VydmVkLldlQ2hhdCBTYW5zIFN0ZCBNZWRpdW1SZWd1bGFySGFueWkgV2VDaGF0IFNhbnMgU3RkLU1lZGl1bTsgVmVyc2lvbiAxLjAwV2VDaGF0IFNhbnMgU3RkLU1lZGl1bVZlcnNpb24gMS4wMFdlQ2hhdC1TYW5zLVN0ZC1NZWRpdW1XZUNoYXQgU2FucyBpcyBhIHRyYWRlbWFyayBvZiBUZW5jZW50LkhhbnlpIEZvbnRzWkhBTkcgWHVhbiwgV0FORyBUaWFuYmksIExJVSBYaWFveXVodHRwOi8vd3d3LmhhbnlpLmNvbS5jbi9XZUNoYXQgU2FucyBTdGRNZWRpdW0gwqzCoiTCoyDCqcKlCjEyMzQ1Njc4OTAAQwBvAHAAeQByAGkAZwBoAHQAIAAoAGMAKQAgADIAMAAxADcAIABiAHkAIABUAGUAbgBjAGUAbgB0AC4AIABBAGwAbAAgAHIAaQBnAGgAdABzACAAcgBlAHMAZQByAHYAZQBkAC4AVwBlAEMAaABhAHQAIABTAGEAbgBzACAAUwB0AGQAIABNAGUAZABpAHUAbQBSAGUAZwB1AGwAYQByAEgAYQBuAHkAaQAgAFcAZQBDAGgAYQB0ACAAUwBhAG4AcwAgAFMAdABkAC0ATQBlAGQAaQB1AG0AOwAgAFYAZQByAHMAaQBvAG4AIAAxAC4AMAAwAFcAZQBDAGgAYQB0ACAAUwBhAG4AcwAgAFMAdABkAC0ATQBlAGQAaQB1AG0AVgBlAHIAcwBpAG8AbgAgADEALgAwADAAVwBlAEMAaABhAHQALQBTAGEAbgBzAC0AUwB0AGQALQBNAGUAZABpAHUAbQBXAGUAQwBoAGEAdAAgAFMAYQBuAHMAIABpAHMAIABhACAAdAByAGEAZABlAG0AYQByAGsAIABvAGYAIABUAGUAbgBjAGUAbgB0AC4ASABhAG4AeQBpACAARgBvAG4AdABzAFoASABBAE4ARwAgAFgAdQBhAG4ALAAgAFcAQQBOAEcAIABUAGkAYQBuAGIAaQAsACAATABJAFUAIABYAGkAYQBvAHkAdQBoAHQAdABwADoALwAvAHcAdwB3AC4AaABhAG4AeQBpAC4AYwBvAG0ALgBjAG4ALwBXAGUAQwBoAGEAdAAgAFMAYQBuAHMAIABTAHQAZABNAGUAZABpAHUAbQAgAKwAogAkAKMAIACpAKUACgAxADIAMwA0ADUANgA3ADgAOQAwAAAAAAIAAAAAAAD/tQAyAAAAAAAAAAAAAAAAAAAAAAAAAA4ADgAAABMAFAAVABYAFwAYABkAGgAbABwAEQAHAQIHdW5pRkZFNQAA) format("truetype")}.rich_media_wrp{position:relative}.pay button{width:182px;height:40px;line-height:40px;background-color:#fa9d3b;color:#fff;font-size:17px;border:0;border-radius:4px;font-weight:500;position:relative;outline:0;font-family:-apple-system-font,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Hiragino Sans GB","Microsoft YaHei UI","Microsoft YaHei",Arial,sans-serif;overflow:hidden}.pay button .price{font-family:"WeChatSansStd-Medium"}.pay button:not(.btn_disabled):active::after{content:"";position:absolute;left:0;right:0;bottom:0;top:0;background-color:rgba(0,0,0,0.1)}.pay button.btn_disabled{background-color:#f2f2f2;color:rgba(0,0,0,0.18)}.pay__mask{position:absolute;width:100%;left:0;bottom:0;text-align:center}.pay__notice{visibility:hidden;opacity:0;padding:16px;width:100%;box-sizing:border-box;position:fixed;bottom:0;background:#f4f4f4;padding-bottom:calc(16px + constant(safe-area-inset-bottom));padding-bottom:calc(16px + env(safe-area-inset-bottom));z-index:100;-webkit-transition:all .3s;transition:all .3s}.pay__notice button.btn_disabled{background-color:#fff}.pay__notice_show{visibility:visible;opacity:1}.pay__notice-intro{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:top;-webkit-align-items:top;align-items:top}.pay__intro-content{-webkit-box-flex:1;-webkit-flex:1;flex:1;font-size:14px;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.pay__intro-content .pay__notice-desc{font-size:12px;color:rgba(0,0,0,0.3);line-height:17px}.pay__notice-title{line-height:20px;font-size:17px}.pay__notice-main{color:rgba(0,0,0,0.3);padding-right:30px;font-size:17px;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center;height:54px}.pay__notice-close{position:absolute;right:0;top:0;padding:16px;font-size:0}.pay__notice-close::before{content:"";display:inline-block;vertical-align:middle;width:24px;height:24px;background-size:cover;background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='c4adbcb4-e5f6-47ae-8835-e10a689c1c34-a' d='M8 6.943L1.807.75.75 1.807 6.943 8 .75 14.193l1.057 1.057L8 9.057l6.193 6.193 1.057-1.057L9.057 8l6.193-6.193L14.193.75z'/%3E  %3C/defs%3E  %3Cuse fill-opacity='.9' fill-rule='evenodd' opacity='.3' transform='translate(4 4)' xlink:href='%23c4adbcb4-e5f6-47ae-8835-e10a689c1c34-a'/%3E%3C/svg%3E")}.pay__worth{-webkit-appearance:none;-webkit-tap-highlight-color:rgba(0,0,0,0);outline:0;background-color:transparent;border:0;display:inline-block;vertical-align:middle;padding:0;font-size:15px;line-height:2.13333333;color:#576b95}.pay__worth::before{content:"";display:inline-block;margin-top:-0.25em;vertical-align:middle;width:20px;height:20px;background-size:cover;background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h20v20H0z'/%3E    %3Cg transform='translate(1.667 3.333)'%3E      %3Cpath stroke='%23576B95' stroke-width='.833' d='M1.963 6.053h-.707c-.417 0-.84.434-.84.944v6.518c0 .488.429 1.17.7 1.17h9.304c.63 0 1.498-.764 2.057-1.945l.139-.288a25.38 25.38 0 0 0 .848-1.975c.372-.98.658-1.932.827-2.82.025-.13.047-.26.067-.387.142-.926-.626-1.704-1.245-1.704h-4.3l.021-.436c.007-.137.023-.28.05-.467l.078-.507c.08-.542.12-.993.12-1.546 0-1.223-.684-2.045-1.52-2.17-.835-.124-1.525.192-1.525.731 0 1.51-.166 2.366-.89 3.567-.335.556-.832.927-1.436 1.138a3.983 3.983 0 0 1-1.659.19c-.068-.006-.12-.013-.089-.013z'/%3E      %3Cpath fill='%23576B95' d='M2.332 6.079h1v8.471h-1z'/%3E    %3C/g%3E    %3Cpath stroke='%23576B95' stroke-width='.667' d='M13.189 4.167c.425.174.79.412 1.094.716.304.304.543.67.717 1.095a3.29 3.29 0 0 1 .717-1.095 3.29 3.29 0 0 1 1.094-.716 3.29 3.29 0 0 1-1.094-.717A3.29 3.29 0 0 1 15 2.356a3.29 3.29 0 0 1-.717 1.094 3.29 3.29 0 0 1-1.094.717z'/%3E  %3C/g%3E%3C/svg%3E")}.pay__worth_ed::before{display:inline-block;vertical-align:middle;width:20px;height:20px;background-size:cover;background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h20v20H0z'/%3E    %3Cg transform='translate(1.667 3.333)'%3E      %3Cpath fill='%23576B95' stroke='%23576B95' stroke-width='.833' d='M1.963 6.053h-.707c-.417 0-.84.434-.84.944v6.518c0 .488.429 1.17.7 1.17h9.304c.63 0 1.498-.764 2.057-1.945l.139-.288a25.38 25.38 0 0 0 .848-1.975c.372-.98.658-1.932.827-2.82.025-.13.047-.26.067-.387.142-.926-.626-1.704-1.245-1.704h-4.3l.021-.436c.007-.137.023-.28.05-.467l.078-.507c.08-.542.12-.993.12-1.546 0-1.223-.684-2.045-1.52-2.17-.835-.124-1.525.192-1.525.731 0 1.51-.166 2.366-.89 3.567-.335.556-.832.927-1.436 1.138a3.983 3.983 0 0 1-1.659.19c-.068-.006-.12-.013-.089-.013z'/%3E      %3Crect width='1.11' height='8.471' x='2.332' y='6.079' fill='%23FFF' rx='.555'/%3E    %3C/g%3E    %3Cpath fill='%23576B95' stroke='%23576B95' stroke-width='.667' d='M13.189 4.167c.425.174.79.412 1.094.716.304.304.543.67.717 1.095a3.29 3.29 0 0 1 .717-1.095 3.29 3.29 0 0 1 1.094-.716 3.29 3.29 0 0 1-1.094-.717A3.29 3.29 0 0 1 15 2.356a3.29 3.29 0 0 1-.717 1.094 3.29 3.29 0 0 1-1.094.717z'/%3E  %3C/g%3E%3C/svg%3E")}.pay__tag{background-color:rgba(250,157,59,0.1);color:#fa9d3b;border-radius:2px;font-size:12px;padding:2px 6px;line-height:17px;vertical-align:middle;margin-top:-2.5px;display:inline-block;margin-left:8px;font-weight:normal}.pay_disabled .pay__worth{color:rgba(0,0,0,0.5)}.pay_disabled .pay__worth::before{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20'%3E  %3Cg fill='none' fill-rule='evenodd' opacity='.5'%3E    %3Cpath d='M0 0h20v20H0z'/%3E    %3Cg transform='translate(1.667 3.333)'%3E      %3Cpath stroke='%23000' stroke-width='.833' d='M1.963 6.053h-.707c-.417 0-.84.434-.84.944v6.518c0 .488.429 1.17.7 1.17h9.304c.63 0 1.498-.764 2.057-1.945l.139-.288a25.38 25.38 0 0 0 .848-1.975c.372-.98.658-1.932.827-2.82.025-.13.047-.26.067-.387.142-.926-.626-1.704-1.245-1.704h-4.3l.021-.436c.007-.137.023-.28.05-.467l.078-.507c.08-.542.12-.993.12-1.546 0-1.223-.684-2.045-1.52-2.17-.835-.124-1.525.192-1.525.731 0 1.51-.166 2.366-.89 3.567-.335.556-.832.927-1.436 1.138a3.983 3.983 0 0 1-1.659.19c-.068-.006-.12-.013-.089-.013z'/%3E      %3Cpath fill='%23000' d='M2.332 6.079h1v8.471h-1z'/%3E    %3C/g%3E    %3Cpath stroke='%23000' stroke-width='.667' d='M13.189 4.167c.425.174.79.412 1.094.716.304.304.543.67.717 1.095a3.29 3.29 0 0 1 .717-1.095 3.29 3.29 0 0 1 1.094-.716 3.29 3.29 0 0 1-1.094-.717A3.29 3.29 0 0 1 15 2.356a3.29 3.29 0 0 1-.717 1.094 3.29 3.29 0 0 1-1.094.717z'/%3E  %3C/g%3E%3C/svg%3E")}.pay__detail-wrp_inner{padding-bottom:48px;margin-bottom:-15px}.pay__detail{text-align:center;padding:0 16px;border-radius:4px;position:relative}.pay__detail-head{line-height:72px;font-weight:500;font-size:17px;display:-webkit-box;display:-webkit-flex;display:flex;position:relative}.pay__detail-head::after{content:"";display:block;position:absolute;left:0;bottom:0;border-bottom:1px solid rgba(0,0,0,0.1);-webkit-transform:scaleY(0.5);transform:scaleY(0.5);width:100%;-webkit-transform-origin:left bottom;transform-origin:left bottom}.pay__detail-title{-webkit-box-flex:1;-webkit-flex:1;flex:1}.pay__detail-wall{font-size:0;margin-right:-8px}.pay__detail-wall img{width:32px;height:32px;margin-right:6.75px;margin-bottom:8px;border-radius:2px}.pay__detail-wall-wrp{line-height:1;margin-bottom:-8px}.pay__detail-summary{display:inline-block;margin-bottom:16px;line-height:20px;font-size:14px;position:relative}.pay__detail-summary a{padding:0 10px;margin:0 -5px 0 -10px}.pay__detail-summary:before,.pay__detail-summary:after{content:"";display:block;position:absolute;width:48px;top:50%;-webkit-transform:translateY(-50%) scaleY(0.5);transform:translateY(-50%) scaleY(0.5);border-top:1px solid rgba(0,0,0,0.1)}.pay__detail-summary:before{left:-64px}.pay__detail-summary:after{right:-64px}.pay__detail-rate{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.pay__detail-rate-item{width:48px;height:48px;background-color:rgba(255,255,255,0.5);border-radius:50%;margin-right:24px;position:relative}.pay__detail-rate-item:last-child{margin-right:0}.pay__rate-positive::before{content:"";position:absolute;display:inline-block;left:13px;top:11px;width:24px;height:24px;background-size:cover;background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cg transform='translate(2 4)'%3E      %3Cpath stroke='%23576B95' d='M2.356 7.264h-.848c-.5 0-1.008.52-1.008 1.133v7.821c0 .586.514 1.404.84 1.404h11.163c.756 0 1.799-.916 2.47-2.334l.166-.345a30.455 30.455 0 0 0 1.017-2.37c.447-1.178.79-2.32.993-3.384.03-.158.057-.313.08-.465.17-1.112-.75-2.045-1.494-2.045h-5.158l.024-.523a5.69 5.69 0 0 1 .06-.56c.015-.107.08-.518.093-.609.097-.65.145-1.192.145-1.854 0-1.469-.821-2.455-1.824-2.604-1.003-.15-1.83.23-1.83.876 0 1.813-.2 2.84-1.069 4.28-.402.668-.998 1.113-1.723 1.366a4.78 4.78 0 0 1-1.99.228c-.082-.007-.144-.015-.107-.015z'/%3E      %3Cpath fill='%23576B95' d='M2.799 7.295h1V17.46h-1z'/%3E    %3C/g%3E    %3Cpath stroke='%23576B95' stroke-width='.8' d='M15.827 5c.51.209.948.495 1.313.86s.651.803.86 1.313a3.95 3.95 0 0 1 .86-1.313A3.948 3.948 0 0 1 20.173 5a3.948 3.948 0 0 1-1.313-.86A3.948 3.948 0 0 1 18 2.827a3.95 3.95 0 0 1-.86 1.313 3.948 3.948 0 0 1-1.313.86z'/%3E  %3C/g%3E%3C/svg%3E")}.pay__rate-positive.active::before{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cg transform='translate(2 4)'%3E      %3Cpath fill='%23576B95' stroke='%23576B95' d='M2.356 7.264h-.848c-.5 0-1.008.52-1.008 1.133v7.821c0 .586.514 1.404.84 1.404h11.163c.756 0 1.799-.916 2.47-2.334l.166-.345a30.455 30.455 0 0 0 1.017-2.37c.447-1.178.79-2.32.993-3.384.03-.158.057-.313.08-.465.17-1.112-.75-2.045-1.494-2.045h-5.158l.024-.523a5.69 5.69 0 0 1 .06-.56c.015-.107.08-.518.093-.609.097-.65.145-1.192.145-1.854 0-1.469-.821-2.455-1.824-2.604-1.003-.15-1.83.23-1.83.876 0 1.813-.2 2.84-1.069 4.28-.402.668-.998 1.113-1.723 1.366a4.78 4.78 0 0 1-1.99.228c-.082-.007-.144-.015-.107-.015z'/%3E      %3Cpath fill='%23FFF' d='M2.799 7.295h1V17.46h-1z'/%3E    %3C/g%3E    %3Cpath fill='%23576B95' stroke='%23576B95' stroke-width='.8' d='M15.827 5c.51.209.948.495 1.313.86s.651.803.86 1.313a3.95 3.95 0 0 1 .86-1.313A3.948 3.948 0 0 1 20.173 5a3.948 3.948 0 0 1-1.313-.86A3.948 3.948 0 0 1 18 2.827a3.95 3.95 0 0 1-.86 1.313 3.948 3.948 0 0 1-1.313.86z'/%3E  %3C/g%3E%3C/svg%3E")}.pay__rate-negative::before{content:"";position:absolute;display:inline-block;left:14px;top:15px;width:24px;height:24px;background-size:cover;background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd' transform='matrix(1 0 0 -1 0 24)'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cg transform='translate(2 4)'%3E      %3Cpath stroke='%23576B95' d='M2.356 7.264h-.848c-.5 0-1.008.52-1.008 1.133v7.821c0 .586.514 1.404.84 1.404h11.163c.756 0 1.799-.916 2.47-2.334l.166-.345a30.455 30.455 0 0 0 1.017-2.37c.447-1.178.79-2.32.993-3.384.03-.158.057-.313.08-.465.17-1.112-.75-2.045-1.494-2.045h-5.158l.024-.523a5.69 5.69 0 0 1 .06-.56c.015-.107.08-.518.093-.609.097-.65.145-1.192.145-1.854 0-1.469-.821-2.455-1.824-2.604-1.003-.15-1.83.23-1.83.876 0 1.813-.2 2.84-1.069 4.28-.402.668-.998 1.113-1.723 1.366a4.78 4.78 0 0 1-1.99.228c-.082-.007-.144-.015-.107-.015z'/%3E      %3Cpath fill='%23576B95' d='M2.799 7.295h1V17.46h-1z'/%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E")}.pay__rate-negative.active::before{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd' transform='matrix(1 0 0 -1 0 24)'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cg transform='translate(2 4)'%3E      %3Cpath fill='%23576B95' stroke='%23576B95' d='M2.356 7.264h-.848c-.5 0-1.008.52-1.008 1.133v7.821c0 .586.514 1.404.84 1.404h11.163c.756 0 1.799-.916 2.47-2.334l.166-.345a30.455 30.455 0 0 0 1.017-2.37c.447-1.178.79-2.32.993-3.384.03-.158.057-.313.08-.465.17-1.112-.75-2.045-1.494-2.045h-5.158l.024-.523a5.69 5.69 0 0 1 .06-.56c.015-.107.08-.518.093-.609.097-.65.145-1.192.145-1.854 0-1.469-.821-2.455-1.824-2.604-1.003-.15-1.83.23-1.83.876 0 1.813-.2 2.84-1.069 4.28-.402.668-.998 1.113-1.723 1.366a4.78 4.78 0 0 1-1.99.228c-.082-.007-.144-.015-.107-.015z'/%3E      %3Cpath fill='%23FFF' d='M2.799 7.295h1V17.46h-1z'/%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E")}.pay__summary{padding:16px 32px 48px;color:rgba(0,0,0,0.5)}.pay__summary-head{font-weight:500;line-height:22.4px;margin-bottom:12px;font-size:17px}.pay__empty-notice{color:rgba(0,0,0,0.3);text-align:center;margin:110px 0 57px}.pay__summary-content{line-height:28px;white-space:pre-wrap;font-size:17px}.pay__detail-wrp_v2 .pay__detail{padding:0 32px}.pay__detail-wrp_v2 .pay__detail-wall{display:inline-block;text-align:left}.pay__detail-wrp_v2 .pay__detail-wall img{margin-right:8px}.pay__worth-action{text-align:center}.pay__icon-worth{display:inline-block;width:48px;height:48px;border-radius:50%;position:relative;background-color:rgba(0,0,0,0.02)}.pay__icon-worth::before{content:"";left:11px;top:9px;position:absolute;display:inline-block;vertical-align:middle;width:28px;height:28px;background-size:cover;background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h28v28H0z'/%3E    %3Cg transform='translate(2.333 4.667)'%3E      %3Cpath stroke='%23576B95' stroke-width='1.167' d='M2.748 8.475H1.76c-.584 0-1.176.606-1.176 1.321v9.125c0 .683.6 1.638.98 1.638h13.024c.882 0 2.099-1.069 2.881-2.723l.194-.403a35.53 35.53 0 0 0 1.187-2.765c.52-1.373.922-2.705 1.158-3.948.035-.183.066-.364.094-.543.199-1.296-.876-2.385-1.743-2.385H12.34l.03-.61c.008-.192.03-.392.068-.654.018-.124.093-.603.11-.71.113-.759.17-1.39.17-2.163 0-1.713-.96-2.864-2.13-3.038-1.17-.174-2.135.268-2.135 1.022 0 2.115-.232 3.313-1.247 4.995-.469.777-1.164 1.297-2.01 1.592a5.576 5.576 0 0 1-2.322.266c-.095-.008-.167-.017-.125-.017z'/%3E      %3Cpath fill='%23576B95' d='M3.265 8.511h1.167V20.37H3.265z'/%3E    %3C/g%3E    %3Cpath stroke='%23576B95' stroke-width='.933' d='M18.464 5.833a4.606 4.606 0 0 1 1.533 1.004A4.6 4.6 0 0 1 21 8.369a4.606 4.606 0 0 1 1.003-1.532c.426-.426.938-.76 1.533-1.004a4.606 4.606 0 0 1-1.533-1.003A4.606 4.606 0 0 1 21 3.298a4.606 4.606 0 0 1-1.003 1.532c-.426.426-.938.76-1.533 1.003z'/%3E  %3C/g%3E%3C/svg%3E")}.pay__icon-worth_active::before{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h20v20H0z'/%3E    %3Cg transform='translate(1.667 3.333)'%3E      %3Cpath fill='%23576B95' stroke='%23576B95' stroke-width='.833' d='M1.963 6.053h-.707c-.417 0-.84.434-.84.944v6.518c0 .488.429 1.17.7 1.17h9.304c.63 0 1.498-.764 2.057-1.945l.139-.288a25.38 25.38 0 0 0 .848-1.975c.372-.98.658-1.932.827-2.82.025-.13.047-.26.067-.387.142-.926-.626-1.704-1.245-1.704h-4.3l.021-.436c.007-.137.023-.28.05-.467l.078-.507c.08-.542.12-.993.12-1.546 0-1.223-.684-2.045-1.52-2.17-.835-.124-1.525.192-1.525.731 0 1.51-.166 2.366-.89 3.567-.335.556-.832.927-1.436 1.138a3.983 3.983 0 0 1-1.659.19c-.068-.006-.12-.013-.089-.013z'/%3E      %3Crect width='1.11' height='8.471' x='2.332' y='6.079' fill='%23FFF' rx='.555'/%3E    %3C/g%3E    %3Cpath fill='%23576B95' stroke='%23576B95' stroke-width='.667' d='M13.189 4.167c.425.174.79.412 1.094.716.304.304.543.67.717 1.095a3.29 3.29 0 0 1 .717-1.095 3.29 3.29 0 0 1 1.094-.716 3.29 3.29 0 0 1-1.094-.717A3.29 3.29 0 0 1 15 2.356a3.29 3.29 0 0 1-.717 1.094 3.29 3.29 0 0 1-1.094.717z'/%3E  %3C/g%3E%3C/svg%3E")}.pay__worth-desc{color:#576b95;font-size:14px;line-height:20px}.pay__desc{font-size:14px;line-height:20px;margin-top:12px;text-align:center;color:rgba(0,0,0,0.3);margin-bottom:-8px}.pay__notice-btn-wrp{position:relative}.pay__notice-qrcode{display:none;position:absolute;left:50%;-webkit-transform:translateX(-50%);transform:translateX(-50%);bottom:70px;width:218px;padding:40px 0;background-color:#fff;box-shadow:0 1px 9px rgba(0,0,0,0.2);border-radius:4px;text-align:center}.pay__qrcode-wrp{height:124px}.pay__qrcode-wrp img{width:124px}.pay__qrcode-title{margin-top:20px;font-size:14px}.pay__static{position:relative;z-index:10;text-align:center;padding-bottom:48px;margin-bottom:-15px}.pay__static h3{padding-top:40px;font-size:17px;margin-bottom:4px;font-weight:500}.pay__static p{font-size:14px;color:rgba(0,0,0,0.3)}.pay__static button{margin-top:36px;outline:0}.pay__static button:active{outline:0}.pay__static .pay__notice-qrcode_bottom{top:90px;bottom:auto}.pay__static .pay__detail{margin-bottom:0}.pay__mask_static{margin-top:-120px;height:120px;position:relative;background:-webkit-gradient(linear,left top,left bottom,from(rgba(255,255,255,0)),to(#fff));background:linear-gradient(to bottom,rgba(255,255,255,0),#fff);pointer-events:none}@media screen and (min-width:1024px){.pay__notice{padding:35px 0}.pay__notice-intro{max-width:677px;padding:0 40px;margin:0 auto;box-sizing:border-box;position:relative}}.pay__detail-wrp{margin-top:40px}.pay__main+.pay__detail-wrp{margin-top:48px;margin-bottom:0;padding-bottom:0}@media(prefers-color-scheme:dark){.pay button{background-color:#c77d2f;color:rgba(255,255,255,0.8)}.pay__tag{background-color:rgba(149,92,33,0.35);color:#fa9d3b}.pay__summary{color:rgba(255,255,255,0.5)}.pay__empty-notice{color:rgba(255,255,255,0.5)}.pay__mask_static{background:-webkit-gradient(linear,left top,left bottom,from(rgba(35,35,35,0)),to(#232323));background:linear-gradient(to bottom,rgba(35,35,35,0),#232323)}.pay button.btn_disabled{background-color:rgba(255,255,255,0.08);color:rgba(255,255,255,0.2)}.pay .pay__notice button.btn_disabled{background-color:rgba(255,255,255,0.08);color:rgba(255,255,255,0.2)}.pay button:not(.btn_disabled):active{position:relative}.pay button:not(.btn_disabled):active::after{content:"";display:block;position:absolute;left:0;right:0;bottom:0;top:0;background-color:rgba(0,0,0,0.1)}.pay__detail-summary::before,.pay__detail-summary::after{border-color:rgba(255,255,255,0.1)}.pay__detail-summary{color:rgba(255,255,255,0.5)}.pay__notice{background-color:#2f2f2f}}@media(prefers-color-scheme:dark){.icon_appmsg_tag{background-color:rgba(255,255,255,0.15);color:rgba(255,255,255,0.5)}.icon_appmsg_tag.appmsg_title_tag{background:rgba(255,255,255,0.05);color:rgba(255,255,255,0.5)}body{color:rgba(255,255,255,0.8)}.tips_global_primary.tips_global_primary{color:rgba(255,255,255,0.3)}.weapp_text_link:before{background-image:url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAA8CAMAAAANIilAAAAAh1BMVEUvLy8AAAAvLy92iJ9CR00vLy8vLy8vLy8wMDAvLy8wMDAwMDA8PDwyMzQ6PEA2Nzp6jaUvLy8vLy8wMDAwMDAzMzNHTFUuLi57j6dzhJlvf5RqeItAREo9QER1hpxndYdebHtKUFldaHZRWWRPV2ExMTFseo9lcoNYYm9VX2xaZXI3Nzd9kKkeLDk8AAAALHRSTlP1APH+9+XAvJptRT0I9fb2/tesoHUZ+Bb+/f389/b9/Pv4+vn5Ffz7+vn6F2FjkhUAAAIWSURBVEjHpZfdcqowEID3RP4hgIhQURTUWnu67/98XWZqIQmkYfJdcZFvsmw2yQb+zZJEZeBtXcbcrReUUTI/ak6uQ5+BAPPD2kiOCzJVWBH/Kcc+LOLHWnm/Ay27/bIcufAHbrQkh2BAOCsnARgRJKr87oEh3rssJ+Qa24kkB7CCQJRDWEU4lSNYSTTKe3et7O5/5R2sZveSY9CRPpsNbo6fGQjEP7KvUXmHP+Sf4i4ZZP3EWYMjFy5NTXKhkR/kHG5O5twO9NXBhGKQa7bs3sm4chjgV/p2YITVJOvqo6FY4cUF8UOsFNClK6PJTvDihLgRUwaJJmoanvMx8W+IfBp3ArrKdIS5OMUh1iiUxnJFiYcJpAamMqfF+g8TSPUM5ZYyfxaqhNTtbKYySa6OSFQwhVRXMdMupxUS5DsSeQ8CpCor1edIOIJM9fF2SUGCKfINiXMvhp0+7xkoMDnsliqhqYSELeLKCaPEHDmYyVtpqVL6uRQMZU8qkp4mBkOZ1FLewJ1QkGeNXEobg4Y38MsT8aGRI2lLZpTsk1jNi7BEPgw+KNJ0/MZ2WfaVYyjNh0OW9Kw/kHuFZUL1AKwocPI3OHDUuKyeOXqdM764co1czB76/PZAYtO1oCNeum5422agx1cvOnNimyvW6nK3aStsGhqbVsqqibNpH20aV4uW2aZZt34m2D9Q7J9GKl+mjzKr5+A3+MAynHfP5MYAAAAASUVORK5CYII=')}.appmsg_card_context{background-color:#2f2f2f}.appmsg_card_active:active{background-color:#2d2d2d}.share_mod_context .share_mod_hd:before{border-color:rgba(255,255,255,0.08)}.appmsg_skin_default .rich_media_area_primary{background-color:#232323}.appmsg_skin_default .rich_media_area_primary .weui-loadmore_line{border-color:rgba(255,255,255,0.08)}.appmsg_skin_default .rich_media_area_primary .weui-loadmore_line .weui-loadmore__tips{color:rgba(255,255,255,0.3);background:#232323}body{background-color:#191919}body a{color:#7d90a9}.rich_media_meta_link{color:#7d90a9}.rich_media_content{color:rgba(255,255,255,0.8)}.rich_media_meta_text,.icon_appmsg_tag.default,.reward_area_win .reward_user_tips .weui-loadmore__tips a,.simple_pagination,.sp_page_current,blockquote,.blockquote_info{color:rgba(255,255,255,0.3)}blockquote{border-color:#606060}.img_loading{background-color:#2f2f2f!important;border-color:#2f2f2f!important}.original_primary_nickname,.original_panel_content,.original_panel_title{color:rgba(255,255,255,0.8)}.original_primary_tips,.original_primary_desc,.original_panel .original_account_nickname{color:rgba(255,255,255,0.5)}.original_primary_card,.original_primary_card_tips{color:rgba(255,255,255,0.3)}.original_primary_card .weui-flex__ft:after{background-image:url("data:image/svg+xml;charset=utf8, %3Csvg width='10' height='20' viewBox='0 0 10 20' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Cdefs%3E%3Cpath d='M6.323 10.358l-.884.884L.623 6.426a.83.83 0 0 1 0-1.177L5.44.433l.884.884-4.52 4.52 4.52 4.521z' id='a'/%3E%3C/defs%3E%3Cuse fill='%23FFF' transform='rotate(-180 4.184 7.921)' xlink:href='%23a' fill-rule='evenodd' opacity='.3' /%3E%3C/svg%3E")}.original_panel{background-color:#2f2f2f}.original_panel_tool a{color:#7d90a9}}</style>
<style>
        </style>
<!--[if lt IE 9]>
<link rel="stylesheet" type="text/css" href="//res.wx.qq.com/mmbizwap/zh_CN/htmledition/style/page/appmsg_new/pc492bcc.css">
<![endif]-->

    </head>
                        <body id="activity-detail" class="zh_CN   mm_appmsg
 discuss_tab  appmsg_skin_default appmsg_style_default ">
        <!-- <span style="color: red">currentVersion </span>
                <div style="color:red;padding-left: 50px;">is IOS</div>
                 -->

        
<script nonce="567503264" type="text/javascript">
    var biz = "MjM5NDg5MjExMQ=="||"";
    var sn = "763df4247d40384132e0a6b5361275a5" || ""|| "";
    var mid = "2650775174" || ""|| "";
    var idx = "1" || "" || "";
    window.__allowLoadResFromMp = true; 
    
        
</script>
<script nonce="567503264" type="text/javascript">
var page_begintime=+new Date,is_rumor="",norumor="";
1*is_rumor&&!(1*norumor)&&biz&&mid&&(document.referrer&&-1!=document.referrer.indexOf("mp.weixin.qq.com/mp/rumor")||(location.href="http://mp.weixin.qq.com/mp/rumor?action=info&__biz="+biz+"&mid="+mid+"&idx="+idx+"&sn="+sn+"#wechat_redirect"));
</script>
<script nonce="567503264" type="text/javascript">
var MutationObserver=window.WebKitMutationObserver||window.MutationObserver||window.MozMutationObserver,isDangerSrc=function(t){
if(t){
var e=t.match(/http(?:s)?:\/\/([^\/]+?)(\/|$)/);
if(e&&!/qq\.com(\:8080)?$/.test(e[1])&&!/weishi\.com$/.test(e[1]))return!0;
}
return!1;
},ishttp=0==location.href.indexOf("http://");
-1==location.href.indexOf("safe=0")&&ishttp&&"function"==typeof MutationObserver&&"mp.weixin.qq.com"==location.host&&(window.__observer_data={
count:0,
exec_time:0,
list:[]
},window.__observer=new MutationObserver(function(t){
window.__observer_data.count++;
var e=new Date,r=[];
t.forEach(function(t){
for(var e=t.addedNodes,o=0;o<e.length;o++){
var n=e[o];
if("SCRIPT"===n.tagName){
var i=n.src;
isDangerSrc(i)&&(window.__observer_data.list.push(i),r.push(n)),!i&&window.__nonce_str&&n.getAttribute("nonce")!=window.__nonce_str&&(window.__observer_data.list.push("inlinescript_without_nonce"),
r.push(n));
}
}
});
for(var o=0;o<r.length;o++){
var n=r[o];
n.parentNode&&n.parentNode.removeChild(n);
}
window.__observer_data.exec_time+=new Date-e;
}),window.__observer.observe(document,{
subtree:!0,
childList:!0
})),function(){
if(-1==location.href.indexOf("safe=0")&&Math.random()<.01&&ishttp&&HTMLScriptElement.prototype.__lookupSetter__&&"undefined"!=typeof Object.defineProperty){
window.__danger_src={
xmlhttprequest:[],
script_src:[],
script_setAttribute:[]
};
var t="$"+Math.random();
HTMLScriptElement.prototype.__old_method_script_src=HTMLScriptElement.prototype.__lookupSetter__("src"),
HTMLScriptElement.prototype.__defineSetter__("src",function(t){
t&&isDangerSrc(t)&&window.__danger_src.script_src.push(t),this.__old_method_script_src(t);
});
var e="element_setAttribute"+t;
Object.defineProperty(Element.prototype,e,{
value:Element.prototype.setAttribute,
enumerable:!1
}),Element.prototype.setAttribute=function(t,r){
"SCRIPT"==this.tagName&&"src"==t&&isDangerSrc(r)&&window.__danger_src.script_setAttribute.push(r),
this[e](t,r);
};
}
}();
</script>

        <link rel="dns-prefetch" href="//res.wx.qq.com">
<link rel="dns-prefetch" href="//mmbiz.qpic.cn">
<link rel="dns-prefetch" href="https://wxa.wxs.qq.com">
<link rel="shortcut icon" type="image/x-icon" href="//res.wx.qq.com/a/wx_fed/assets/res/NTI4MWU5.ico">
<link rel="mask-icon" href="//res.wx.qq.com/a/wx_fed/assets/res/MjliNWVm.svg" color="#4C4C4C">
<link rel="apple-touch-icon-precomposed" href="//res.wx.qq.com/a/wx_fed/assets/res/OTE0YTAw.png">
<script nonce="567503264" type="text/javascript">
    String.prototype.html = function(encode) {
        var replace =["&#39;", "'", "&quot;", '"', "&nbsp;", " ", "&gt;", ">", "&lt;", "<", "&yen;", "¥", "&amp;", "&"];
        
		
		
		
		
        
        var replaceReverse = ["&", "&amp;", "¥", "&yen;", "<", "&lt;", ">", "&gt;", " ", "&nbsp;", '"', "&quot;", "'", "&#39;"];
	    var target;
	    if (encode) {
	    	target = replaceReverse;
	    } else {
	    	target = replace;
	    }
        for (var i=0,str=this;i< target.length;i+= 2) {
             str=str.replace(new RegExp(target[i],'g'),target[i+1]);
        }
        return str;
    };

    window.isInWeixinApp = function() {
        return /MicroMessenger/.test(navigator.userAgent);
    };

    window.getQueryFromURL = function(url) {
        url = url || 'http://qq.com/s?a=b#rd'; 
        var tmp = url.split('?'),
            query = (tmp[1] || "").split('#')[0].split('&'),
            params = {};
        for (var i=0; i<query.length; i++) {
            var arg = query[i].split('=');
            params[arg[0]] = arg[1];
        }
        if (params['pass_ticket']) {
        	params['pass_ticket'] = encodeURIComponent(params['pass_ticket'].html(false).html(false).replace(/\s/g,"+"));
        }
        return params;
    };

    (function() {
	    var params = getQueryFromURL(location.href);
        window.uin = params['uin'] || "" || '';
        window.key = params['key'] || "" || '';
        window.wxtoken = params['wxtoken'] || '';
        window.pass_ticket = params['pass_ticket'] || '';
        window.appmsg_token = "";
    })();

    function wx_loaderror() {
        if (location.pathname === '/bizmall/reward') {
            new Image().src = '/mp/jsreport?key=96&content=reward_res_load_err&r=' + Math.random();
        }
    }

</script>

<script nonce="567503264" type="text/javascript">
        window.__moon_report_uin = "0";
            window.no_moon_ls = 0;
    </script>

        
<script nonce="567503264" type="text/javascript">
    var write_sceen_time = (+new Date());
</script>

<div id="js_article" class="rich_media">
    
    <div id="js_top_ad_area" class="top_banner"></div>
    
    <div class="rich_media_inner">

        
        
		<div id="page-content" class="rich_media_area_primary">

		  <div class="rich_media_area_primary_inner">

            
                        
                        

            <div id="img-content" class="rich_media_wrp">
                
                <h2 class="rich_media_title" id="activity-name">
                    
                    
                    
这名99后跳下冰河冻得呻吟发抖，他却说......
                </h2>
                <div id="meta_content" class="rich_media_meta_list">
                                                                                
                                        <span class="rich_media_meta rich_media_meta_nickname" id="profileBt">
                      <a href="javascript:void(0);" id="js_name">
                        中国青年网                      </a>
                      <div id="js_profile_qrcode" class="profile_container" style="display:none;">
                          <div class="profile_inner">
                              <strong class="profile_nickname">中国青年网</strong>
                              <img class="profile_avatar" id="js_profile_qrcode_img" src="" alt="">

                              <p class="profile_meta">
                              <label class="profile_meta_label">微信号</label>
                              <span class="profile_meta_value">youthzqw</span>
                              </p>

                              <p class="profile_meta">
                              <label class="profile_meta_label">功能介绍</label>
                              <span class="profile_meta_value">青年温度，青春靓度，青网态度</span>
                              </p>
                              
                          </div>
                          <span class="profile_arrow_wrp" id="js_profile_arrow_wrp">
                              <i class="profile_arrow arrow_out"></i>
                              <i class="profile_arrow arrow_in"></i>
                          </span>
                      </div>
                    </span>
                    <em id="publish_time" class="rich_media_meta rich_media_meta_text"></em>
                </div>
                

                

                

                
                                


                
                
                
                
                                                
                                                                
                                
                                
                
                <div class="rich_media_content " id="js_content" style="visibility: hidden;">
                    

                    

                    
                    
                    <section class="xmteditor" style="display:none;" data-tools="新媒体管家" data-label="powered by xmt.cn"><br  /></section><section style="box-sizing: border-box;font-size: 16px;"><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.11625" data-src="https://mmbiz.qpic.cn/mmbiz_gif/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkhCia3zdViaDYnBnXNXc9EIDOJcOiaaEwxP1yd4g2z1mQVKOkXSsDVf1icA/640?wx_fmt=gif" data-type="gif" data-w="800" style="vertical-align: middle;box-sizing: border-box;"></section></section><section style="box-sizing: border-box;" powered-by="xiumi.us"><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;">今天</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">微博、抖音热搜榜上</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">都出现了一位消防员的身影</p></section><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.4537037" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkAJlSI1JuxiaUVu4ySeHosl7aJJ2Iadt0AwUiapAKDkicZJBmTOrF3TWaw/640?wx_fmt=jpeg" data-type="jpeg" data-w="1080" style="vertical-align: middle;box-sizing: border-box;"></section></section><section style="box-sizing: border-box;" powered-by="xiumi.us"><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;">他的视频被发布到网上后</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">仅抖音上的观看人数</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">就超过了千万</p></section><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.2908623" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkSkSiaZaNL1icaHPagoSxZj3GibCoCduwuzxQQyN37AjwD3e1gd3hUWnyw/640?wx_fmt=jpeg" data-type="jpeg" data-w="777" style="vertical-align: middle;box-sizing: border-box;"></section></section><section style="box-sizing: border-box;" powered-by="xiumi.us"><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;">戳视频<img data-ratio="1" data-src="https://mmbiz.qpic.cn/mmbiz_png/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkW7DGdLDCaPvYcIRjFETet1jqWHTlUd52Oia1aIibqUxCe4mRBBxNZyPg/640?wx_fmt=png" data-type="png" data-w="18" style="width:18px;display: inline-block;vertical-align: text-bottom;"></p></section><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;" powered-by="xiumi.us"><section style="width: 100%;background-color: rgb(0, 0, 0);line-height: 0;box-sizing: border-box;"><section class="video-box" style="width: 100%;height: 100%;transform: rotate(0deg);box-sizing: border-box;"><iframe frameborder="0" allowfullscreen="" scrolling="no" class="video_iframe" data-vidtype="-1" data-ratio="1.7777777777777777" data-w="640" data-src="https://v.qq.com/iframe/preview.html?width=500&amp;height=375&amp;auto=0&amp;vid=f304640gl1z"> &amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;nbsp;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578193563260_0.6231338412056155&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578193563327_0.060254889704980164&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578193563394_0.13487972761417355&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578193563461_0.07451760081681136&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578193563528_0.4135345389352296&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578193563595_0.8783070119654182&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578193563663_0.9352175628418249&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578193563783_0.056683632086030444&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578194613808_0.09130377507066756&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578194651481_0.9273883380482908&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578194651589_0.10083337023222527&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578194651697_0.19033202821523676&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578194651805_0.7726972260966201&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578194651915_0.25648781596916015&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;mpchecktext contenteditable=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;false&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot; id=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;1578194652025_0.5677827964630262&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;quot;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt;/mpchecktext&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;gt;</iframe> &nbsp;<section class="video-cover" style="top: 0px;left: 0px;width: 100%;height: 40%;box-sizing: border-box;"><br  /></section></section></section></section><section style="box-sizing: border-box;" powered-by="xiumi.us"><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;">这名消防员</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">就是徐桂敏</p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;">近日，河南气温跌破冰点</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">有群众却不慎落水</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">1999年出生的</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">消防员徐桂敏</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">忍受着刺骨的冰水</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">下水救人</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">回到岸上后</p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><strong><span style="color: rgb(0, 122, 170);">冰水浸湿了衣服</span></strong></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><strong><span style="color: rgb(0, 122, 170);">在零下的温度里</span></strong></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><strong><span style="color: rgb(0, 122, 170);">他被冻得躺在地上</span></strong></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><strong><span style="color: rgb(0, 122, 170);">一边发抖</span></strong></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><strong><span style="color: rgb(0, 122, 170);">一边发出呻吟</span></strong></p><p style="text-align: center;white-space: normal;box-sizing: border-box;">虽然立马有人给他盖上了衣服</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">但还是很难缓解</p></section><p style="text-align: center;"><img class="rich_pages" data-ratio="0.7993197278911565" data-src="https://mmbiz.qpic.cn/mmbiz_gif/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkdSjqI15rn4ibns1CiaKgNxL81PkeqYQI7FmibJ5icOSkiaUsshLSntHDU5A/640?wx_fmt=gif" data-type="gif" data-w="294" style=""></p><section style="box-sizing: border-box;" powered-by="xiumi.us"><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;">他的身体被冻得僵硬</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">行走困难</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">被两个人搀扶着</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">才回到车上</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">路上还不停地全身发抖</p></section><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.8717949" data-src="https://mmbiz.qpic.cn/mmbiz_gif/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkow62mM7fW85kLS7F2SlI3XCfUa4GHg1TA709lvAo2qerlTaX88APKQ/640?wx_fmt=gif" data-type="gif" data-w="312" style="vertical-align: middle;box-sizing: border-box;"></section></section><section style="box-sizing: border-box;" powered-by="xiumi.us"><p style="text-align: center;"><br  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;">周围的群众看到他的样子</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">心疼地直呼：</p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><span style="color: rgb(0, 122, 170);"><strong>“娃儿，我的娃儿呀…”</strong></span></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;">但他却没有感到委屈</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">事后，徐桂敏说：</p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><span style="color: rgb(0, 122, 170);"><strong>“下水的一瞬间，</strong></span></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><span style="color: rgb(0, 122, 170);"><strong>感觉脑子一炸，</strong></span></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><span style="color: rgb(0, 122, 170);"><strong>浑身冰凉，</strong></span></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><span style="color: rgb(0, 122, 170);"><strong>可是我顾不上寒冷了，</strong></span></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><span style="color: rgb(0, 122, 170);"><strong>就想着人离我没有几米远，</strong></span></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><span style="color: rgb(0, 122, 170);"><strong>赶紧游过去，</strong></span></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><span style="color: rgb(0, 122, 170);"><strong>哪怕早一秒，</strong></span></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><span style="color: rgb(0, 122, 170);"><strong>也有几分生还的机会。</strong></span><span style="color: rgb(0, 122, 170);"><strong>”</strong></span></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;">对于众多网友的关心</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">他也做出了回应：</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">“把人救上岸后，</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">厨师煮了姜茶给我喝，</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">又泡了热水澡，</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">现在身体没有什么呢不舒服，</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">谢谢大家关心！”</p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><strong>这名99后感动了众多网友</strong></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><strong>也引来无数称赞与心疼</strong></p></section><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.1685185" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkma9ribvibpjlHYEBIuV4YIHC620ia0erZ8xicZibV6Mv4yB4KYfXUXJa8eg/640?wx_fmt=jpeg" data-type="jpeg" data-w="1080" style="vertical-align: middle;box-sizing: border-box;"></section></section><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.1092593" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdk19qXQfGYZEAC8Lt1DHnurTAWwAWj41bscrm0icPh3vOibQWa67QD2DMg/640?wx_fmt=jpeg" data-type="jpeg" data-w="1080" style="vertical-align: middle;box-sizing: border-box;"></section></section><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.1203704" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdknPBUrenibgMswtmRiconyj0dHzKsxlLNfYhPseAGn8qicB7OjSJrGsAqw/640?wx_fmt=jpeg" data-type="jpeg" data-w="1080" style="vertical-align: middle;box-sizing: border-box;"></section></section><section style="box-sizing: border-box;" powered-by="xiumi.us"><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><strong>有人则看到了年轻一代的</strong></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><strong>责任与担当</strong></p></section><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.1416667" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdk8kV07uxd6picKsufz4j1WLQucFf7DJyWsQaqLCta8Re3x4WvEuAOpbA/640?wx_fmt=jpeg" data-type="jpeg" data-w="1080" style="vertical-align: middle;box-sizing: border-box;"></section></section><section style="box-sizing: border-box;" powered-by="xiumi.us"><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.1203704" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkk8PT56zIzibniaKiapia6DziaBPYzNHD7ib75uRlVlyvFB4BXT2lWKeoe6Bg/640?wx_fmt=jpeg" data-type="jpeg" data-w="1080" style="vertical-align: middle;box-sizing: border-box;"></section></section></section><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.2111111" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkiauWrjk2HfTwmD5ricmRGdEM7l9ozIJnprWDo2tcbuvvSTbdD4GTyRpw/640?wx_fmt=jpeg" data-type="jpeg" data-w="1080" style="vertical-align: middle;box-sizing: border-box;"></section></section><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.1259259" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdk1L4lc2NzWb1oJUSiapNFtOsoWGdHgWsa3LpoYK9Led39ZEq1ia1wAiamQ/640?wx_fmt=jpeg" data-type="jpeg" data-w="1080" style="vertical-align: middle;box-sizing: border-box;"></section></section><section style="box-sizing: border-box;" powered-by="xiumi.us"><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;">虽然身体被冻僵</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">但那颗火热的心</p><p style="text-align: center;white-space: normal;box-sizing: border-box;">却温暖了众人</p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"  /></p><p style="text-align: center;"><span style="color: rgb(0, 122, 170);font-size: 18px;"><strong>点亮“在看”</strong></span><br  /></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><span style="color: rgb(0, 122, 170);font-size: 18px;"><strong>为负重前行的英雄们点赞！</strong></span></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"  /></p></section><section style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.015625" data-src="https://mmbiz.qpic.cn/mmbiz_png/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkMTHoB7wD493A0QtUcPTk7lOq6L6QgdmYGc5MMlUFPcicoDo1L3Q3KSw/640?wx_fmt=png" data-type="png" data-w="640" style="vertical-align: middle;box-sizing: border-box;"></section></section><section style="transform: rotate(0deg);-webkit-transform: rotate(0deg);-moz-transform: rotate(0deg);-o-transform: rotate(0deg);box-sizing: border-box;" powered-by="xiumi.us"><section style="font-size: 14px;color: rgb(160, 160, 160);box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><strong style="box-sizing: border-box;">┃来源：中国青年网综合整理自@人民日报、网友评论</strong></p><p style="white-space: normal;box-sizing: border-box;"><strong style="box-sizing: border-box;">┃责编：张玘云</strong></p><p style="white-space: normal;box-sizing: border-box;"><strong style="box-sizing: border-box;">©中国青年网出品（ID：youthzqw），转载相关文章请注明出处。</strong></p></section></section><section style="margin-top: 10px;margin-right: 0%;margin-left: 0%;box-sizing: border-box;" powered-by="xiumi.us"><section style="display: inline-block;vertical-align: middle;width: 40%;box-sizing: border-box;"><section style="margin-top: 0.5em;margin-bottom: 0.5em;box-sizing: border-box;" powered-by="xiumi.us"><section style="border-top: 1px dashed rgb(231, 195, 219);box-sizing: border-box;height: 0px;line-height: 0;"><br  /></section></section></section><section style="display: inline-block;vertical-align: middle;width: 20%;box-sizing: border-box;"><section style="text-align: center;font-size: 10px;box-sizing: border-box;" powered-by="xiumi.us"><p style="box-sizing: border-box;">长按指纹</p><p style="box-sizing: border-box;">一键关注</p></section></section><section style="display: inline-block;vertical-align: middle;width: 40%;box-sizing: border-box;"><section style="margin-top: 0.5em;margin-bottom: 0.5em;box-sizing: border-box;" powered-by="xiumi.us"><section style="border-top: 1px dashed rgb(231, 195, 219);box-sizing: border-box;height: 0px;line-height: 0;"><br  /></section></section></section></section><section style="margin-right: 0%;margin-bottom: 10px;margin-left: 0%;box-sizing: border-box;" powered-by="xiumi.us"><section style="display: inline-block;vertical-align: middle;width: 50%;box-sizing: border-box;"><section style="text-align: center;margin-right: 0%;margin-left: 0%;transform: translate3d(0px, 0px, 0px);box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 80%;box-sizing: border-box;"><img class="raw-image" data-ratio="1" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkEvE28ibthkqYnGVfMibAialQCb5lxqpcAxjgntO216SMuo6m4qicLts9eQ/640?wx_fmt=jpeg" data-type="jpeg" data-w="258" style="vertical-align: middle;width: 100%;box-sizing: border-box;"></section></section></section><section style="display: inline-block;vertical-align: middle;width: 50%;box-sizing: border-box;"><section style="text-align: center;margin: 10px 0%;opacity: 0.67;transform: translate3d(0px, 0px, 0px);-webkit-transform: translate3d(0px, 0px, 0px);-moz-transform: translate3d(0px, 0px, 0px);-o-transform: translate3d(0px, 0px, 0px);box-sizing: border-box;" powered-by="xiumi.us"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 70%;box-sizing: border-box;"><img class="raw-image" data-ratio="0.9066667" data-src="https://mmbiz.qpic.cn/mmbiz_png/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkcN7aLv3VkiaibhdLXjvwgenvia1fQMMaolrshRowj7x1C2rNrzQWqYNcg/640?wx_fmt=png" data-type="png" data-w="150" style="vertical-align: middle;width: 100%;box-sizing: border-box;"></section></section></section></section><section style="margin-top: 10px;margin-right: 0%;margin-left: 0%;text-align: right;box-sizing: border-box;" powered-by="xiumi.us"><section style="display: inline-block;vertical-align: middle;box-sizing: border-box;"><section style="display: inline-block;vertical-align: bottom;padding-left: 5px;padding-right: 5px;line-height: 1.2em;margin-bottom: 2px;color: rgb(170, 70, 62);box-sizing: border-box;"><p style="box-sizing: border-box;">点一下你会更好看耶</p></section><section style="max-width: 100%;display: inline-block;vertical-align: bottom;line-height: 0;width: 1.6em;box-sizing: border-box;"><img class="raw-image" data-ratio="0.8808777" data-src="https://mmbiz.qpic.cn/mmbiz_gif/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkicFte6icJiauv739zyBR6YAFh1dHgXM5dl9lC2uFSC8WvtKpmOsoCkwgA/640?wx_fmt=gif" data-type="gif" data-w="638" style="vertical-align: middle;width: 100%;box-sizing: border-box;"></section></section></section></section><p><br  /></p>
				</div>

                
                				

                <script nonce="567503264" type="text/javascript">
                    var first_sceen__time = (+new Date());

                    if ("" == 1 && document.getElementById('js_content')) {
                        document.getElementById('js_content').addEventListener("selectstart",function(e){ e.preventDefault(); });
                    }

                    
                    (function(){
                        if (navigator.userAgent.indexOf("WindowsWechat") != -1){
                            var link = document.createElement('link');
                            var head = document.getElementsByTagName('head')[0];
                            link.rel = 'stylesheet';
                            link.type = 'text/css';
                            link.href = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/style/page/appmsg_new/winwx492bcc.css";
                            head.appendChild(link);
                        }
                    })();
                </script>

                
<div class="ct_mpda_wrp" id="js_sponsor_ad_area" style="display: none;"></div>


                
                <div class="read-more__area" id="js_more_read_area" style="display:none;">
                    
                </div>

                 
                                                </div>
                                        
                                

                        
            <ul id="js_hotspot_area" class="article_extend_area"></ul>


            

            

    <div class="rich_media_tool" id="js_toobar3">
  <div class="weui-flex">
    <div class="weui-flex__item">
                  
                  <div id="js_read_area3" class="media_tool_meta tips_global_primary meta_primary" style="display:none;">
        <span id="readTxt">阅读</span>
        <span id="readNum3"></span>
      </div>
          </div>

            <span style="display:none;" class="media_tool_meta meta_extra meta_praise" id="like_old">
          <i class="icon_praise_gray"></i><span class="praise_num" id="likeNum_old"></span>
      </span>

          
  <span style="visibility: hidden;" class="media_tool_meta meta_extra meta_like" id="like3">
  <button class="like_btn" id="js_like_btn"> 
    <span id="js_like_wording">在看</span><span class="like_num" id="likeNum3"></span>
  </button>
</span>

          
        </div> 

</div>


  
  <div class="like_comment_wrp" id="js_like_comment" style="display: none;">
    <div class="like_comment_inner">
      <div class="like_comment_hd" style="display:none" id="js_like_title"></div>
      <div class="like_comment_bd">
        <div class="like_comment_tips" id="js_comment_area">
          <i class="weui-icon-success"></i><i class="icon-success-primary"></i>已同步到看一看<a href="javascript:;" class="like_comment_share_link" id="js_like_comment_share">写下你的想法</a>
        </div>
        <div class="like_comment_extra_info" id="js_like_educate" style="display: none">
          <p class="like_comment_extra_tips">
            <span id="js_friend_like_area" style="display: none"></span>
            <span id="js_friend_like_word">前往“发现”-“看一看”浏览“朋友在看”</span>
          </p>
          <p class="like_comment_pic_wrp">
                          <img class="like_comment_pic" src="//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/pic/appmsg/pic_like_comment492329.png">
                      </p>
          <button class="weui-btn weui-btn_primary" id="js_go_wow">前往看一看</button>
        </div>
      </div>
    </div>
  </div>
  <div style="display:none;" id="wow_close_inform">
    <div class="weui-mask"></div>
    <div class="weui-dialog">
      <div class="weui-dialog__hd"><strong class="weui-dialog__title">看一看入口已关闭</strong></div>
      <div class="weui-dialog__bd">
        在“设置”-“通用”-“发现页管理”打开“看一看”入口      </div>
      <div class="weui-dialog__ft" id="wow_close_ack">
        <a href="javascript:;" class="weui-dialog__btn weui-dialog__btn_primary">我知道了</a>
      </div>
    </div>
  </div>

<div id="js_like_toast" style="display: none;">
  <div class="weui-mask_transparent"></div>
  <div class="weui-toast">
    <i class="weui-icon-success-no-circle weui-icon_toast"></i>
    <p class="weui-toast__content" id="js_toast_msg">已发送</p>
  </div>
</div>

<div style="display: none;" id="js_comment_panel">
  <div class="like_comment_primary_wrp editing" id="js_comment_wrp">
    <div class="like_comment_primary_inner">
      <div class="like_comment_primary_hd">
        <div class="like_comment_primary_hd_side">
          <button class="like_comment_primary_cancel" id="js_comment_cancel">
            取消            <i class="weui-icon-close-thin"></i>
          </button>
        </div>
        <h4 class="like_comment_primary_title"> 发送到看一看 </h4>
        <div class="like_comment_primary_hd_side">
          <button class="like_comment_primary_btn" id="js_comment_confirm" disabled="disabled">发送</button>
        </div>
      </div>
      <div class="like_comment_primary_bd">
        <div class="like_comment_media_title" id="js_panel_like_title">
                      这名99后跳下冰河冻得呻吟发抖，他却说......
                  </div>
        <textarea class="like_comment_textarea weui-textarea" placeholder="写下你的想法..." id="js_comment_text"></textarea>
      </div>
      <span class="like_comment_msg" id="js_like_comment_msg" style="visibility: hidden;">最多200字，当前共<span id="js_like_current_cnt"></span>字</span>
    </div>
  </div>
  <div class="like_comment_primary_mask" id="js_mask_2"></div>
</div>

<div id="js_loading" style="display: none;">
    <div class="weui-mask_transparent"></div>
    <div class="weui-toast">
        <i class="weui-loading weui-icon_toast"></i>
        <p class="weui-toast__content">发送中</p>
    </div>
</div>



                      </div>
        </div>

        <div class="rich_media_area_primary sougou" id="sg_tj" style="display:none"></div>


        
        <div class="rich_media_area_extra">
          <div class="rich_media_area_extra_inner">
              
              <div id="js_share_appmsg">
              </div>

              

<div class="mpda_bottom_container" id="js_bottom_ad_area"></div>
              
              <div id="js_iframetest" style="display:none;"></div>
                            
              <div class="rich_media_extra rich_media_extra_discuss" id="js_cmt_container" style="display:none">
                

                
                <div class="discuss_mod" id="js_friend_cmt_area" style="display:none">
                  
                  
                  
                </div>

                                <div class="discuss_mod" id="js_cmt_area" style="display:none">
                </div>
                              </div>

              <div class="function_mod function_mod_index" id="js_related_area" style="display:none;">
                <div class="function_hd">相关阅读</div>
                <div class="function_bd">
                    <div id="js_related"></div>
                    <a href="javascript:;" class="weui-media-box weui-media-box_loadmore hide" id="js_related_load_more">
                      <div class="weui-media-box__bd">更多文章</div>
                      <div class="weui-media-box__ft"></div>
                    </a>
                </div>
              </div>
          </div>
        </div>

        
        <div id="js_pc_qr_code" class="qr_code_pc_outer" style="display:none;">
            <div class="qr_code_pc_inner">
                <div class="qr_code_pc">
                    <img id="js_pc_qr_code_img" class="qr_code_pc_img">
                    <p>微信扫一扫<br>关注该公众号</p>
                </div>
            </div>
        </div>
    </div>
</div>



<div id="js_pc_weapp_code" class="weui-desktop-popover weui-desktop-popover_pos-up-center weui-desktop-popover_img-text" style="display: none;">
    <div class="weui-desktop-popover__content">
        <div class="weui-desktop-popover__desc">
            <img id="js_pc_weapp_code_img">
            微信扫一扫<br>使用小程序<span id="js_pc_weapp_code_des"></span>        </div>
    </div>
</div>
<div id="js_minipro_dialog" style="display:none;">
    <div class="weui-mask"></div>
    <div class="weui-dialog weui-dialog_link">
        <div class="weui-dialog__hd">
            <strong class="weui-dialog__title" id="js_minipro_dialog_head"></strong>
        </div>
        <div class="weui-dialog__bd" id="js_minipro_dialog_body"></div>
        
        <div class="weui-dialog__ft">
            <a id="js_minipro_dialog_cancel" href="javascript:void(0);" class="weui-dialog__btn weui-dialog__btn_default">取消</a>
            <a id="js_minipro_dialog_ok" href="javascript:void(0);" class="weui-dialog__btn weui-dialog__btn_primary">允许</a>
        </div>
    </div>
</div>
<div id="js_link_dialog" style="display:none;">
    <div class="weui-mask"></div>
    <div class="weui-dialog weui-dialog_link">
        <div class="weui-dialog__hd">
            <strong class="weui-dialog__title" id="js_link_dialog_head"></strong>
        </div>
        <div class="weui-dialog__bd" id="js_link_dialog_body"></div>
        
        <div class="weui-dialog__ft">
            <a id="js_link_dialog_cancel" href="javascript:void(0);" class="weui-dialog__btn weui-dialog__btn_default">取消</a>
            <a id="js_link_dialog_ok" href="javascript:void(0);" class="weui-dialog__btn weui-dialog__btn_primary">允许</a>
        </div>
    </div>
</div>


<div class="comment_primary_emotion_panel_wrp" id="js_emotion_panel_pc" style="display: none">
  <div class="comment_primary_emotion_panel">
    <ul class="comment_primary_emotion_list" id="js_emotion_list_pc">
    </ul>
  </div>
</div>


<div class="weui-dialog__wrp" id="js_alert_panel" style="display:none;">
  <div class="weui-mask"></div>
  <div class="weui-dialog">
    <div class="weui-dialog__bd" id="js_alert_content"></div>
    <div class="weui-dialog__ft">
      <a href="javascript:;" class="weui-dialog__btn weui-dialog__btn_default" id="js_alert_confirm">知道了</a>
    </div>
  </div>
</div>

<div id="js_weapp_without_auth_dialog" style="display:none;">
    <div class="weui-mask"></div>
    <div class="weui-dialog weui-dialog_link">
        <div class="weui-dialog__bd" id="js_weapp_without_auth_dialog_name"></div>
        <div class="weui-dialog__ft">
            <a id="js_weapp_without_auth_dialog_ok" href="javascript:void(0);" class="weui-dialog__btn weui-dialog__btn_primary">确定</a>
        </div>
    </div>
</div>

<script nonce="567503264" type="text/javascript">
var PAGE_MID='mmbizwap:appmsg/newindex.html';
</script>
        <script nonce="567503264" type="text/javascript">
window.logs.pagetime.page_begin = Date.now();
</script>
        <script nonce="567503264" type="text/javascript">
  (function () {
    
    var ajaxWhiteList = {
      1: { 
        reg: /^https?:\/\/mp\.weixin\.qq\.com\/mp\/appmsg_like/,
        times: 0
      },
      2: { 
        reg: /^https?:\/\/mp\.weixin\.qq\.com\/mp\/appmsg_comment((\?|&)[^=]*?=[^&]*?)*?(\?|&)action=likecomment/,
        times: 0
      },
      3: { 
        reg: /^https?:\/\/mp\.weixin\.qq\.com\/mp\/appmsg_comment((\?|&)[^=]*?=[^&]*?)*?(\?|&)action=addcomment/,
        times: 0
      },
      4: { 
        reg: /^https?:\/\/mp\.weixin\.qq\.com\/mp\/authorreward/,
        times: 0
      }
      
      
      
      
    };

    
    if (!performance || !performance.getEntries) return;

    
    var hasReported = false;

    
    var reportResLoadTime = function () {
      
      if (hasReported) return;

      
      var notSupport = false;

      
      var ajaxEntries = [];

      
      var entries = performance.getEntries().map(function (entry) {
        if (typeof entry !== 'object') {
          notSupport = true;
        } else if (entry.entryType === undefined) {
          notSupport = true;
        } else if (
          entry.entryType !== 'navigation' &&
          entry.entryType !== 'resource'
        ) {
          
          return null;
        } else if (entry.initiatorType === undefined) {
          notSupport = true;
        } else if (entry.initiatorType === 'xmlhttprequest') {
          
          if (entry.name === undefined || entry.duration === undefined) {
            notSupport = true;
          } else {
            for (var scene in ajaxWhiteList) {
              if (Object.prototype.hasOwnProperty.call(ajaxWhiteList, scene)) {
                var ajaxItem = ajaxWhiteList[scene];
                if (ajaxItem.times < 10 && ajaxItem.reg.test(entry.name)) {
                  ajaxEntries.push({
                    scene: scene,
                    protocol: entry.nextHopProtocol,
                    is_https: isHttps(entry),
                    time: entry.duration
                  });
                  ajaxItem.times++;
                }
              }
            }
          }
          return null;
        }
        return entry;
      });

      
      if (notSupport || ajaxEntries.length === 0) return;

      
      var data = {
        stat_list: ajaxEntries
      };
      var img = new Image();
      img.src = 'https://mp.weixin.qq.com/mp/timereport?data=' + JSON.stringify(data);
      hasReported = true;
    };

    
    window.addEventListener('beforeunload', reportResLoadTime, false);
    window.addEventListener('unload', reportResLoadTime, false);

    function isHttps(entry) {
      if (/^https/.test(entry.name)) return 1;
      else return 0;
    }
  })();
</script>
        <script nonce="567503264">
    var __DEBUGINFO = {
        debug_js : "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/debug/console42f400.js",
        safe_js : "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/safe/moonsafe42f400.js",
        res_list: []
    };
</script>

<script nonce="567503264" type="text/javascript">
(function() {
	var totalCount = 0,
			finishCount = 0;

	function _loadVConsolePlugin() {
		window.vConsole = new window.VConsole();
		while (window.vConsolePlugins.length > 0) {
			var p = window.vConsolePlugins.shift();
			window.vConsole.addPlugin(p);
		}
	}
	
	function _addVConsole(uri, cb) {
		totalCount++;
		var node = document.createElement('SCRIPT');
		node.type = 'text/javascript';
		node.src = uri;
		node.setAttribute('nonce', '567503264');
		if (cb) {
			node.onload = cb;
		}
		document.getElementsByTagName('head')[0].appendChild(node);
	}
	if (
		(document.cookie && document.cookie.indexOf('vconsole_open=1') > -1)
		|| location.href.indexOf('vconsole=1') > -1
	) {
		window.vConsolePlugins = [];
		_addVConsole('//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/vconsole/3.2.2/vconsole.min440203.js', function() {
			
			_addVConsole('//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/vconsole/plugin/vconsole-mpopt/1.0.1/vconsole-mpopt42f400.js', _loadVConsolePlugin);
		});
	}

  
  try {
    var adIframeUrl = localStorage.getItem('__WXLS_ad_iframe_url');
    if (window === top) {
      if (adIframeUrl) {
        if (navigator.userAgent.indexOf('iPhone') > -1) {
          var img = new Image();
          img.src = adIframeUrl;
        } else {
          var link = document.createElement('link');
          link.rel = 'prefetch';
          link.href = adIframeUrl;
          document.getElementsByTagName('head')[0].appendChild(link);
        }
      }
    }
  } catch (err) {

  }

})();
</script>
        
<script nonce="567503264" type="text/javascript">
if (location.href.match(/fontScale=\d+/) && /(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {

    var m=location.href.match(/fontScale=(\d*)/);
    var map={
        "94":1,
        "100":2,
        "109":3,
        "119":4,
        "131":5,
    }
    if(m&&m[1]&&map[m[1]]){
        document.getElementsByTagName("body")[0].className+=" appmsg_skin_fontscale_"+map[m[1]];
        console.log("appmsg_skin_fontscale_:"+map[m[1]]);
    }
}
</script>
<script nonce="567503264" type="text/javascript">
function _typeof(e){
return e&&"undefined"!=typeof Symbol&&e.constructor===Symbol?"symbol":typeof e;
}
!function(e){
if("object"===("undefined"==typeof module?"undefined":_typeof(module)))module.exports=e;else{
if(window.__second_open__)return;
var t="1578540388",n="1578198176",s="2020-01-05";
e(t,n,s,document.getElementById("publish_time"));
}
}(function(e,t,n,s){
var i="",o=86400,f=new Date(1e3*e),r=1*t,l=n||"";
f.setHours(0),f.setMinutes(0),f.setSeconds(0);
var c=f.getTime()/1e3;
f.setDate(1),f.setMonth(0);
var u=f.getTime()/1e3;
if(r>=c)i="今天";else if(r>=c-o)i="昨天";else if(r>=c-2*o)i="前天";else if(r>=c-3*o)i="3天前";else if(r>=c-4*o)i="4天前";else if(r>=c-5*o)i="5天前";else if(r>=c-6*o)i="6天前";else if(r>=c-14*o)i="1周前";else if(r>=u){
var d=l.split("-");
i="%s月%s日".replace("%s",parseInt(d[1],10)).replace("%s",parseInt(d[2],10));
}else i=l;
s&&(s.innerText=i,setTimeout(function(){
s.onclick=function(){
s.innerText=l;
};
},10));
});
</script>
<script nonce="567503264" type="text/javascript">

if (!window.console) window.console = { log: function() {} };

if (typeof getComputedStyle == 'undefined') {
    if (document.body.currentStyle) {
        window.getComputedStyle = function(el) {
            return el.currentStyle;
        }
    } else {
        window.getComputedStyle = {};
    }
}

(function(){
    window.__zoom = 1;
    
    (function(){
        var validArr = ","+([0.875, 1, 1.125, 1.25, 1.375]).join(",")+",";
        var match = window.location.href.match(/winzoom=(\d+(?:\.\d+)?)/);
        if (match && match[1]) {
            var winzoom = parseFloat(match[1]);
            if (validArr.indexOf(","+winzoom+",")>=0) {
                window.__zoom = winzoom;
            }
        }
    })();

    var ua = navigator.userAgent.toLowerCase();
    var re = new RegExp("msie ([0-9]+[\.0-9]*)");
    var version;
    if (re.exec(ua) != null) {
        version = parseInt(RegExp.$1);
    }
    var isIE = false;
    if (typeof version != 'undefined' && version >= 6 && version <= 9) {
        isIE = true;
    }
    var getMaxWith=function(){
        var container = document.getElementById('img-content');
        var max_width = container.offsetWidth;
        var container_padding = 0;
        var container_style = getComputedStyle(container);
        container_padding = parseFloat(container_style.paddingLeft) + parseFloat(container_style.paddingRight);
        max_width -= container_padding;
        if (!max_width) {
            max_width = window.innerWidth - 30;      
        }
        return max_width;
    };
    var getParentWidth = function(dom){
        var parent_width = 0;
        var parent = dom.parentNode;
        var outerWidth = 0;
        while (true) {
            if(!parent||parent.nodeType!=1) break;
            var parent_style = getComputedStyle(parent);
            if (!parent_style) break;
            parent_width = parent.clientWidth - parseFloat(parent_style.paddingLeft) - parseFloat(parent_style.paddingRight) - outerWidth;
            if (parent_width > 0) break;
            outerWidth += parseFloat(parent_style.paddingLeft) + parseFloat(parent_style.paddingRight) + parseFloat(parent_style.marginLeft) + parseFloat(parent_style.marginRight) + parseFloat(parent_style.borderLeftWidth) + parseFloat(parent_style.borderRightWidth);
            parent = parent.parentNode;
        }
        return parent_width;
    }
    var getOuterW=function(dom){
        var style=getComputedStyle(dom),
            w=0;
        if(!!style){
            w = parseFloat(style.paddingLeft) + parseFloat(style.paddingRight) + parseFloat(style.borderLeftWidth) + parseFloat(style.borderRightWidth);
        }
        return w;
    };
    var getOuterH =function(dom){
        var style=getComputedStyle(dom),
            h=0;
        if(!!style){
            h = parseFloat(style.paddingTop) + parseFloat(style.paddingBottom) + parseFloat(style.borderTopWidth) + parseFloat(style.borderBottomWidth);
        }
        return h;
    };
    var insertAfter = function(dom,afterDom){
        var _p = afterDom.parentNode;
        if(!_p){
            return;
        }
        if(_p.lastChild === afterDom){
            _p.appendChild(dom);
        }else{
            _p.insertBefore(dom,afterDom.nextSibling);
        }
    };
    var getQuery = function(name,url){
        
        var u  = arguments[1] || window.location.search,
            reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)"),
            r = u.substr(u.indexOf("\?")+1).match(reg);
        return r!=null?r[2]:"";
    };

    
    function setImgSize(item, widthNum, widthUnit, ratio, breakParentWidth) {
        setTimeout(function () {
            var img_padding_border = getOuterW(item) || 0;
            var img_padding_border_top_bottom = getOuterH(item) || 0;
            
            if (widthNum > getParentWidth(item) && !breakParentWidth) {
                widthNum = getParentWidth(item);
            }

            height = (widthNum - img_padding_border) * ratio + img_padding_border_top_bottom;

            if (isIE) {
                var url = item.getAttribute('data-src');
                item.src = url;
            } else {
                if(parseFloat(widthNum, 10) > 40 && height > 40 && breakParentWidth) {
                    item.className += ' img_loading';
                }
                item.src = "data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==";
            }
            item.style.cssText += ";width: " + widthNum + widthUnit + " !important;";
            item.style.cssText += ";height: " + height + widthUnit + " !important;";
        }, 10);
    }
    
    (function(){
        var images = document.getElementsByTagName('img');
        var length = images.length;
        var max_width = getMaxWith();
        for (var i = 0; i < length; ++i) {
            if (window.__second_open__ && images[i].getAttribute('__sec_open_place_holder__')) {
                continue;
            }
            var imageItem = images[i];
            var src_ = imageItem.getAttribute('data-src');
            var realSrc = imageItem.getAttribute('src');
            if (!src_ || realSrc) continue;
            
            var originWidth = imageItem.getAttribute('data-w');
            var ratio_ = 1 * imageItem.getAttribute('data-ratio');

            var height = 100;
            if (ratio_ && ratio_ > 0) {
                var parent_width = getParentWidth(imageItem) || max_width;
                var initWidth = imageItem.style.width || imageItem.getAttribute('width') || originWidth || parent_width;
                initWidth = parseFloat(initWidth, 10) > max_width ? max_width : initWidth;
                
                if (initWidth) {
                    imageItem.setAttribute('_width', !isNaN(initWidth * 1) ? initWidth + 'px' : initWidth);
                }
                
                if (typeof initWidth === 'string' && initWidth.indexOf('%') !== -1) {
                    initWidth = parseFloat(initWidth.replace('%', ''), 10) / 100 * parent_width;
                }
                
                if (initWidth === 'auto') {
                    initWidth = originWidth;
                }

                var res = /^(\d+(?:\.\d+)?)([a-zA-Z%]+)?$/.exec(initWidth);
                var widthNum = res && res.length >= 2 ? res[1] : 0;
                var widthUnit = res && res.length >= 3 && res[2] ? res[2] : 'px';

                
                setImgSize(imageItem, widthNum, widthUnit, ratio_, true);
                
                (function (item, widthNumber, unit, ratio) {
                    setTimeout(function () {
                        setImgSize(item, widthNumber, unit, ratio, false);
                    });
                })(imageItem, widthNum, widthUnit, ratio_);
            } else {
                imageItem.style.cssText += ";visibility: hidden !important;";
            }

        }
    })();
    window.__videoDefaultRatio=16/9;
    window.__getVideoWh = function(dom){
        var max_width = getMaxWith(),
            width = max_width,
            ratio_ = dom.getAttribute('data-ratio')*1,
            arr = [4/3, 16/9],
            ret = arr[0],
            abs = Math.abs(ret - ratio_);
        if (!ratio_) { 
            if (dom.getAttribute("data-mpvid")) { 
                ratio_ = 16/9;
            } else { 
                ratio_ = 4/3;
            }
        } else { 
            for (var j = 1, jl = arr.length; j < jl; j++) {
                var _abs = Math.abs(arr[j] - ratio_);
                if (_abs < abs) {
                    abs = _abs;
                    ret = arr[j];
                }
            }
            ratio_ = ret;
        }

        var parent_width = getParentWidth(dom)||max_width,
            width = width > parent_width ? parent_width : width,
            outerW = getOuterW(dom)||0,
            outerH = getOuterH(dom)||0,
            videoW = width - outerW,
            videoH = videoW/ratio_,
            height = videoH + outerH;
        return {w:Math.ceil(width),h:Math.ceil(height),vh:videoH,vw:videoW,ratio:ratio_};
    };

    
    (function(){
        var iframe = document.getElementsByTagName('iframe');
        for (var i=0,il=iframe.length;i<il;i++) {
            if (window.__second_open__ && iframe[i].getAttribute('__sec_open_place_holder__')) {
                continue;
            }
            var a = iframe[i];
            var src_ = a.getAttribute('src')||a.getAttribute('data-src')||"";
            if(!/^http(s)*\:\/\/v\.qq\.com\/iframe\/(preview|player)\.html\?/.test(src_)
                && !/^http(s)*\:\/\/mp\.weixin\.qq\.com\/mp\/readtemplate\?t=pages\/video_player_tmpl/.test(src_)
            ){
                continue;
            }
            var vid = getQuery("vid",src_);
            if(!vid){
                continue;
            }
            vid=vid.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,"");
            a.removeAttribute('src');
            a.style.display = "none";
            var obj = window.__getVideoWh(a),
                videoPlaceHolderSpan = document.createElement('span'),
                videoPlayerIconSpan = document.createElement('span'),
                mydiv = document.createElement('img');

            videoPlaceHolderSpan.className = "js_img_loading db";
            videoPlaceHolderSpan.setAttribute("data-vid", vid);
            

            videoPlayerIconSpan.className = 'wx_video_context db'; 
            videoPlayerIconSpan.style.display = 'none';
            videoPlayerIconSpan.innerHTML = '<span class="wx_video_thumb_primary"></span><button class="wx_video_play_btn">播放</button><span class="wx_video_mask"></span>'; 

            mydiv.className = "img_loading";

            mydiv.src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==";
            
            
            videoPlaceHolderSpan.style.cssText = "width: " + obj.w + "px !important;";
            mydiv.style.cssText += ";width: " + obj.w + "px";
            videoPlaceHolderSpan.appendChild(videoPlayerIconSpan);
            videoPlaceHolderSpan.appendChild(mydiv);
            insertAfter(videoPlaceHolderSpan, a); 

            a.style.cssText += ";width: " + obj.w + "px !important;";
            a.setAttribute("width",obj.w);
            if(window.__zoom!=1){
                a.style.display = "block";
                videoPlaceHolderSpan.style.display = "none";
                a.setAttribute("_ratio",obj.ratio);
                a.setAttribute("_vid",vid);
            }else{
                videoPlaceHolderSpan.style.cssText += "height: " + obj.h + "px !important;";
                mydiv.style.cssText += "height: " + obj.h + "px !important;";
                a.style.cssText += "height: " + obj.h + "px !important;";
                a.setAttribute("height",obj.h);
            }
            a.setAttribute("data-vh",obj.vh);
            a.setAttribute("data-vw",obj.vw);
            if(a.getAttribute("data-mpvid")){
                a.setAttribute("data-src",location.protocol+"//mp.weixin.qq.com/mp/readtemplate?t=pages/video_player_tmpl&auto=0&vid="+vid);
            }else{
                a.setAttribute("data-src",location.protocol+"//v.qq.com/iframe/player.html?vid="+ vid + "&width="+obj.vw+"&height="+obj.vh+"&auto=0");
            }
        }
    })();

    (function(){
        if(window.__zoom!=1){
            if (!window.__second_open__) {
                document.getElementById('page-content').style.zoom = window.__zoom;
                var a = document.getElementById('activity-name');
                var b = document.getElementById('meta_content');
                if(!!a){
                    a.style.zoom = 1/window.__zoom;
                }
                if(!!b){
                    b.style.zoom = 1/window.__zoom;
                }
            }
            var images = document.getElementsByTagName('img');
            for (var i = 0,il=images.length;i<il;i++) {
                if (window.__second_open__ && images[i].getAttribute('__sec_open_place_holder__')) {
                    continue;
                }
                images[i].style.zoom = 1/window.__zoom;
            }
            var iframe = document.getElementsByTagName('iframe');
            for (var i = 0,il=iframe.length;i<il;i++) {
                if (window.__second_open__ && iframe[i].getAttribute('__sec_open_place_holder__')) {
                    continue;
                }
                var a = iframe[i];
                a.style.zoom = 1/window.__zoom;
                var src_ = a.getAttribute('data-src')||"";
                if(!/^http(s)*\:\/\/v\.qq\.com\/iframe\/(preview|player)\.html\?/.test(src_)
                    && !/^http(s)*\:\/\/mp\.weixin\.qq\.com\/mp\/readtemplate\?t=pages\/video_player_tmpl/.test(src_)
                ){
                    continue;
                }
                var ratio = a.getAttribute("_ratio");
                var vid = a.getAttribute("_vid");
                a.removeAttribute("_ratio");
                a.removeAttribute("_vid");
                var vw = a.offsetWidth - (getOuterW(a)||0);
                var vh = vw/ratio;
                var h = vh + (getOuterH(a)||0)
                a.style.cssText += "height: " + h + "px !important;"
                a.setAttribute("height",h);
                if (/^http(s)*\:\/\/v\.qq\.com\/iframe\/(preview|player)\.html\?/.test(src_)) {
                    a.setAttribute("data-src", location.protocol + "//v.qq.com/iframe/player.html?vid=" + vid + "&width=" + vw + "&height=" + vh + "&auto=0");
                }
                a.style.display = "none";
                var parent = a.parentNode;
                if(!parent){
                    continue;
                }
                for(var j=0,jl=parent.children.length;j<jl;j++){
                    var child = parent.children[j];
                    if(child.className.indexOf("img_loading")>=0 && child.getAttribute("data-vid")==vid){
                        child.style.cssText += "height: " + h + "px !important;";
                        child.style.display = "";
                    }
                }
            }
        }
    })();
})();
</script>
<script nonce="567503264" type="text/javascript">
    
    var whiteList = 'rich_pages,blockquote_info,blockquote_biz,blockquote_other,blockquote_article,js_jump_icon,h5_image_link,js_banner_container,js_list_container,js_cover,js_tx_video_container,js_product_err_container,js_product_loop_content,js_product_container,img_loading,list-paddingleft-1,list-paddingleft-2,list-paddingleft-3,selectTdClass,noBorderTable,ue-table-interlace-color-single,ue-table-interlace-color-double,__bg_gif,weapp_text_link,weapp_image_link,js_img_loading,wx_video_context,db,wx_video_thumb_primary,wx_video_play_btn,wx_video_mask,qqmusic_area,tc,tips_global,unsupport_tips,qqmusic_wrp,appmsg_card_context,appmsg_card_active,qqmusic_bd,play_area,icon_qqmusic_switch,pic_qqmusic_default,qqmusic_thumb,access_area,qqmusic_songname,qqmusic_singername,qqmusic_source,js_audio_frame,share_audio_context,flex_context,pages_reset,share_audio_switch,icon_share_audio_switch,share_audio_info,flex_bd,share_audio_title,share_audio_tips,share_audio_progress_wrp,share_audio_progress,share_audio_progress_inner,share_audio_progress_buffer,share_audio_progress_loading,share_audio_progress_loading_inner,share_audio_progress_handle,share_audio_desc,share_audio_length_current,share_audio_length_total,video_iframe,vote_iframe,js_editor_vote_card,res_iframe,card_iframe,js_editor_card,weapp_display_element,js_weapp_display_element,weapp_card,app_context,weapp_card_bd,weapp_card_profile,radius_avatar,weapp_card_avatar,weapp_card_nickname,weapp_card_info,weapp_card_title,weapp_card_thumb_wrp,weapp_card_ft,weapp_card_logo,js_pay_btn,pay,pay__mask,wx_video_loading'.split(',');
    var qaClassPrefix = 'qa__';
    var dmClassPrefix = 'js_darkmode__';
    var whiteListReg = [
        new RegExp("^weui"),
        new RegExp("^appmsg"),
        new RegExp("^audio"),
        new RegExp("^music"),
        new RegExp("^cps_inner"),
        new RegExp("^bizsvr_"), 
        new RegExp("^code-snippet"), 
        new RegExp("^" + qaClassPrefix), 
        new RegExp("^wx-edui-"), 
        new RegExp('^' + dmClassPrefix), 
    ];
</script>
<script nonce="567503264" type="text/javascript">
function _toConsumableArray(r){
if(Array.isArray(r)){
for(var t=0,e=Array(r.length);t<r.length;t++)e[t]=r[t];
return e;
}
return Array.from(r);
}
function _typeof(r){
return r&&"undefined"!=typeof Symbol&&r.constructor===Symbol?"symbol":typeof r;
}
var _slicedToArray=function(){
function r(r,t){
var e=[],n=!0,a=!1,o=void 0;
try{
for(var i,l=r[Symbol.iterator]();!(n=(i=l.next()).done)&&(e.push(i.value),!t||e.length!==t);n=!0);
}catch(s){
a=!0,o=s;
}finally{
try{
!n&&l["return"]&&l["return"]();
}finally{
if(a)throw o;
}
}
return e;
}
return function(t,e){
if(Array.isArray(t))return t;
if(Symbol.iterator in Object(t))return r(t,e);
throw new TypeError("Invalid attempt to destructure non-iterable instance");
};
}();
!function(r){
var t=r();
t({
whiteListClass:window.whiteList,
whiteListClassReg:window.whiteListReg,
nodes:document.querySelectorAll("#js_content *")
});
}(function(){
var r={
aliceblue:[240,248,255],
antiquewhite:[250,235,215],
aqua:[0,255,255],
aquamarine:[127,255,212],
azure:[240,255,255],
beige:[245,245,220],
bisque:[255,228,196],
black:[0,0,0],
blanchedalmond:[255,235,205],
blue:[0,0,255],
blueviolet:[138,43,226],
brown:[165,42,42],
burlywood:[222,184,135],
cadetblue:[95,158,160],
chartreuse:[127,255,0],
chocolate:[210,105,30],
coral:[255,127,80],
cornflowerblue:[100,149,237],
cornsilk:[255,248,220],
crimson:[220,20,60],
cyan:[0,255,255],
darkblue:[0,0,139],
darkcyan:[0,139,139],
darkgoldenrod:[184,134,11],
darkgray:[169,169,169],
darkgreen:[0,100,0],
darkgrey:[169,169,169],
darkkhaki:[189,183,107],
darkmagenta:[139,0,139],
darkolivegreen:[85,107,47],
darkorange:[255,140,0],
darkorchid:[153,50,204],
darkred:[139,0,0],
darksalmon:[233,150,122],
darkseagreen:[143,188,143],
darkslateblue:[72,61,139],
darkslategray:[47,79,79],
darkslategrey:[47,79,79],
darkturquoise:[0,206,209],
darkviolet:[148,0,211],
deeppink:[255,20,147],
deepskyblue:[0,191,255],
dimgray:[105,105,105],
dimgrey:[105,105,105],
dodgerblue:[30,144,255],
firebrick:[178,34,34],
floralwhite:[255,250,240],
forestgreen:[34,139,34],
fuchsia:[255,0,255],
gainsboro:[220,220,220],
ghostwhite:[248,248,255],
gold:[255,215,0],
goldenrod:[218,165,32],
gray:[128,128,128],
green:[0,128,0],
greenyellow:[173,255,47],
grey:[128,128,128],
honeydew:[240,255,240],
hotpink:[255,105,180],
indianred:[205,92,92],
indigo:[75,0,130],
ivory:[255,255,240],
khaki:[240,230,140],
lavender:[230,230,250],
lavenderblush:[255,240,245],
lawngreen:[124,252,0],
lemonchiffon:[255,250,205],
lightblue:[173,216,230],
lightcoral:[240,128,128],
lightcyan:[224,255,255],
lightgoldenrodyellow:[250,250,210],
lightgray:[211,211,211],
lightgreen:[144,238,144],
lightgrey:[211,211,211],
lightpink:[255,182,193],
lightsalmon:[255,160,122],
lightseagreen:[32,178,170],
lightskyblue:[135,206,250],
lightslategray:[119,136,153],
lightslategrey:[119,136,153],
lightsteelblue:[176,196,222],
lightyellow:[255,255,224],
lime:[0,255,0],
limegreen:[50,205,50],
linen:[250,240,230],
magenta:[255,0,255],
maroon:[128,0,0],
mediumaquamarine:[102,205,170],
mediumblue:[0,0,205],
mediumorchid:[186,85,211],
mediumpurple:[147,112,219],
mediumseagreen:[60,179,113],
mediumslateblue:[123,104,238],
mediumspringgreen:[0,250,154],
mediumturquoise:[72,209,204],
mediumvioletred:[199,21,133],
midnightblue:[25,25,112],
mintcream:[245,255,250],
mistyrose:[255,228,225],
moccasin:[255,228,181],
navajowhite:[255,222,173],
navy:[0,0,128],
oldlace:[253,245,230],
olive:[128,128,0],
olivedrab:[107,142,35],
orange:[255,165,0],
orangered:[255,69,0],
orchid:[218,112,214],
palegoldenrod:[238,232,170],
palegreen:[152,251,152],
paleturquoise:[175,238,238],
palevioletred:[219,112,147],
papayawhip:[255,239,213],
peachpuff:[255,218,185],
peru:[205,133,63],
pink:[255,192,203],
plum:[221,160,221],
powderblue:[176,224,230],
purple:[128,0,128],
rebeccapurple:[102,51,153],
red:[255,0,0],
rosybrown:[188,143,143],
royalblue:[65,105,225],
saddlebrown:[139,69,19],
salmon:[250,128,114],
sandybrown:[244,164,96],
seagreen:[46,139,87],
seashell:[255,245,238],
sienna:[160,82,45],
silver:[192,192,192],
skyblue:[135,206,235],
slateblue:[106,90,205],
slategray:[112,128,144],
slategrey:[112,128,144],
snow:[255,250,250],
springgreen:[0,255,127],
steelblue:[70,130,180],
tan:[210,180,140],
teal:[0,128,128],
thistle:[216,191,216],
tomato:[255,99,71],
turquoise:[64,224,208],
violet:[238,130,238],
wheat:[245,222,179],
white:[255,255,255],
whitesmoke:[245,245,245],
yellow:[255,255,0],
yellowgreen:[154,205,50],
windowtext:[0,0,0]
},t=function(){
function t(r,e){
if(!(this instanceof t))return new t(r,e);
if(e&&e in h&&(e=null),e&&!(e in u))throw new Error("Unknown model: "+e);
var n,a;
if(null==r)this.model="rgb",this.color=[0,0,0],this.valpha=1;else if(r instanceof t)this.model=r.model,
this.color=r.color.slice(),this.valpha=r.valpha;else if("string"==typeof r){
var o=s.get(r);
if(null===o)throw new Error("Unable to parse color from string: "+r);
this.model=o.model,a=u[this.model].channels,this.color=o.value.slice(0,a),this.valpha="number"==typeof o.value[a]?o.value[a]:1;
}else if(r.length){
this.model=e||"rgb",a=u[this.model].channels;
var i=c.call(r,0,a);
this.color=l(i,a),this.valpha="number"==typeof r[a]?r[a]:1;
}else if("number"==typeof r)r&=16777215,this.model="rgb",this.color=[r>>16&255,r>>8&255,255&r],
this.valpha=1;else{
this.valpha=1;
var b=Object.keys(r);
"alpha"in r&&(b.splice(b.indexOf("alpha"),1),this.valpha="number"==typeof r.alpha?r.alpha:0);
var d=b.sort().join("");
if(!(d in f))throw new Error("Unable to parse color from object: "+JSON.stringify(r));
this.model=f[d];
var v=u[this.model].labels,p=[];
for(n=0;n<v.length;n++)p.push(r[v[n]]);
this.color=l(p);
}
if(g[this.model])for(a=u[this.model].channels,n=0;a>n;n++){
var m=g[this.model][n];
m&&(this.color[n]=m(this.color[n]));
}
this.valpha=Math.max(0,Math.min(1,this.valpha)),Object.freeze&&Object.freeze(this);
}
function e(r,t){
return Number(r.toFixed(t));
}
function n(r){
return function(t){
return e(t,r);
};
}
function a(r,t,e){
return r=Array.isArray(r)?r:[r],r.forEach(function(r){
(g[r]||(g[r]=[]))[t]=e;
}),r=r[0],function(n){
var a;
return arguments.length?(e&&(n=e(n)),a=this[r](),a.color[t]=n,a):(a=this[r]().color[t],
e&&(a=e(a)),a);
};
}
function o(r){
return function(t){
return Math.max(0,Math.min(r,t));
};
}
function i(r){
return Array.isArray(r)?r:[r];
}
function l(r,t){
for(var e=0;t>e;e++)"number"!=typeof r[e]&&(r[e]=0);
return r;
}
var s=function(){
function t(r,t,e){
return Math.min(Math.max(t,r),e);
}
function e(r){
var t=r.toString(16).toUpperCase();
return t.length<2?"0"+t:t;
}
var n=r,a=function(){
var r=function(r){
return r&&"string"!=typeof r?r instanceof Array||Array.isArray(r)||r.length>=0&&(r.splice instanceof Function||Object.getOwnPropertyDescriptor(r,r.length-1)&&"String"!==r.constructor.name):!1;
},t=Array.prototype.concat,e=Array.prototype.slice,n=function(n){
for(var a=[],o=0,i=n.length;i>o;o++){
var l=n[o];
r(l)?a=t.call(a,e.call(l)):a.push(l);
}
return a;
};
return n.wrap=function(r){
return function(){
return r(n(arguments));
};
},n;
}(),o={};
for(var i in n)n.hasOwnProperty(i)&&(o[n[i]]=i);
var l={
to:{},
get:{}
};
return l.get=function(r){
var t,e,n=r.substring(0,3).toLowerCase();
switch(n){
case"hsl":
t=l.get.hsl(r),e="hsl";
break;

case"hwb":
t=l.get.hwb(r),e="hwb";
break;

default:
t=l.get.rgb(r),e="rgb";
}
return t?{
model:e,
value:t
}:null;
},l.get.rgb=function(r){
if(!r)return null;
var e,a,o,i=/^#([a-f0-9]{3,4})$/i,l=/^#([a-f0-9]{6})([a-f0-9]{2})?$/i,s=/^rgba?\(\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*(?:,\s*([+-]?[\d\.]+)\s*)?\)$/,u=/^rgba?\(\s*([+-]?[\d\.]+)\%\s*,\s*([+-]?[\d\.]+)\%\s*,\s*([+-]?[\d\.]+)\%\s*(?:,\s*([+-]?[\d\.]+)\s*)?\)$/,c=/(\D+)/,h=[0,0,0,1];
if(e=r.match(l)){
for(o=e[2],e=e[1],a=0;3>a;a++){
var f=2*a;
h[a]=parseInt(e.slice(f,f+2),16);
}
o&&(h[3]=Math.round(parseInt(o,16)/255*100)/100);
}else if(e=r.match(i)){
for(e=e[1],o=e[3],a=0;3>a;a++)h[a]=parseInt(e[a]+e[a],16);
o&&(h[3]=Math.round(parseInt(o+o,16)/255*100)/100);
}else if(e=r.match(s)){
for(a=0;3>a;a++)h[a]=parseInt(e[a+1],0);
e[4]&&(h[3]=parseFloat(e[4]));
}else{
if(!(e=r.match(u)))return(e=r.match(c))?"transparent"===e[1]?[0,0,0,0]:(h=n[e[1]])?(h[3]=1,
h):null:null;
for(a=0;3>a;a++)h[a]=Math.round(2.55*parseFloat(e[a+1]));
e[4]&&(h[3]=parseFloat(e[4]));
}
for(a=0;3>a;a++)h[a]=t(h[a],0,255);
return h[3]=t(h[3],0,1),h;
},l.get.hsl=function(r){
if(!r)return null;
var e=/^hsla?\(\s*([+-]?(?:\d*\.)?\d+)(?:deg)?\s*,\s*([+-]?[\d\.]+)%\s*,\s*([+-]?[\d\.]+)%\s*(?:,\s*([+-]?[\d\.]+)\s*)?\)$/,n=r.match(e);
if(n){
var a=parseFloat(n[4]),o=(parseFloat(n[1])+360)%360,i=t(parseFloat(n[2]),0,100),l=t(parseFloat(n[3]),0,100),s=t(isNaN(a)?1:a,0,1);
return[o,i,l,s];
}
return null;
},l.get.hwb=function(r){
if(!r)return null;
var e=/^hwb\(\s*([+-]?\d*[\.]?\d+)(?:deg)?\s*,\s*([+-]?[\d\.]+)%\s*,\s*([+-]?[\d\.]+)%\s*(?:,\s*([+-]?[\d\.]+)\s*)?\)$/,n=r.match(e);
if(n){
var a=parseFloat(n[4]),o=(parseFloat(n[1])%360+360)%360,i=t(parseFloat(n[2]),0,100),l=t(parseFloat(n[3]),0,100),s=t(isNaN(a)?1:a,0,1);
return[o,i,l,s];
}
return null;
},l.to.hex=function(){
var r=a(arguments);
return"#"+e(r[0])+e(r[1])+e(r[2])+(r[3]<1?e(Math.round(255*r[3])):"");
},l.to.rgb=function(){
var r=a(arguments);
return r.length<4||1===r[3]?"rgb("+Math.round(r[0])+", "+Math.round(r[1])+", "+Math.round(r[2])+")":"rgba("+Math.round(r[0])+", "+Math.round(r[1])+", "+Math.round(r[2])+", "+r[3]+")";
},l.to.rgb.percent=function(){
var r=a(arguments),t=Math.round(r[0]/255*100),e=Math.round(r[1]/255*100),n=Math.round(r[2]/255*100);
return r.length<4||1===r[3]?"rgb("+t+"%, "+e+"%, "+n+"%)":"rgba("+t+"%, "+e+"%, "+n+"%, "+r[3]+")";
},l.to.hsl=function(){
var r=a(arguments);
return r.length<4||1===r[3]?"hsl("+r[0]+", "+r[1]+"%, "+r[2]+"%)":"hsla("+r[0]+", "+r[1]+"%, "+r[2]+"%, "+r[3]+")";
},l.to.hwb=function(){
var r=a(arguments),t="";
return r.length>=4&&1!==r[3]&&(t=", "+r[3]),"hwb("+r[0]+", "+r[1]+"%, "+r[2]+"%"+t+")";
},l.to.keyword=function(r){
return o[r.slice(0,3)];
},l;
}(),u=function(){
function t(r){
var t=function(t){
return void 0===t||null===t?t:(arguments.length>1&&(t=Array.prototype.slice.call(arguments)),
r(t));
};
return"conversion"in r&&(t.conversion=r.conversion),t;
}
function e(r){
var t=function(t){
if(void 0===t||null===t)return t;
arguments.length>1&&(t=Array.prototype.slice.call(arguments));
var e=r(t);
if("object"===("undefined"==typeof e?"undefined":_typeof(e)))for(var n=e.length,a=0;n>a;a++)e[a]=Math.round(e[a]);
return e;
};
return"conversion"in r&&(t.conversion=r.conversion),t;
}
var n=function(){
function t(r,t){
return Math.pow(r[0]-t[0],2)+Math.pow(r[1]-t[1],2)+Math.pow(r[2]-t[2],2);
}
var e=r,n={};
for(var a in e)e.hasOwnProperty(a)&&(n[e[a]]=a);
var o={
rgb:{
channels:3,
labels:"rgb"
},
hsl:{
channels:3,
labels:"hsl"
},
hsv:{
channels:3,
labels:"hsv"
},
hwb:{
channels:3,
labels:"hwb"
},
cmyk:{
channels:4,
labels:"cmyk"
},
xyz:{
channels:3,
labels:"xyz"
},
lab:{
channels:3,
labels:"lab"
},
lch:{
channels:3,
labels:"lch"
},
hex:{
channels:1,
labels:["hex"]
},
keyword:{
channels:1,
labels:["keyword"]
},
ansi16:{
channels:1,
labels:["ansi16"]
},
ansi256:{
channels:1,
labels:["ansi256"]
},
hcg:{
channels:3,
labels:["h","c","g"]
},
apple:{
channels:3,
labels:["r16","g16","b16"]
},
gray:{
channels:1,
labels:["gray"]
}
};
for(var i in o)if(o.hasOwnProperty(i)){
if(!("channels"in o[i]))throw new Error("missing channels property: "+i);
if(!("labels"in o[i]))throw new Error("missing channel labels property: "+i);
if(o[i].labels.length!==o[i].channels)throw new Error("channel and label counts mismatch: "+i);
var l=o[i].channels,s=o[i].labels;
delete o[i].channels,delete o[i].labels,Object.defineProperty(o[i],"channels",{
value:l
}),Object.defineProperty(o[i],"labels",{
value:s
});
}
return o.rgb.hsl=function(r){
var t,e,n,a=r[0]/255,o=r[1]/255,i=r[2]/255,l=Math.min(a,o,i),s=Math.max(a,o,i),u=s-l;
return s===l?t=0:a===s?t=(o-i)/u:o===s?t=2+(i-a)/u:i===s&&(t=4+(a-o)/u),t=Math.min(60*t,360),
0>t&&(t+=360),n=(l+s)/2,e=s===l?0:.5>=n?u/(s+l):u/(2-s-l),[t,100*e,100*n];
},o.rgb.hsv=function(r){
var t,e,n,a,o,i=r[0]/255,l=r[1]/255,s=r[2]/255,u=Math.max(i,l,s),c=u-Math.min(i,l,s),h=function(r){
return(u-r)/6/c+.5;
};
return 0===c?a=o=0:(o=c/u,t=h(i),e=h(l),n=h(s),i===u?a=n-e:l===u?a=1/3+t-n:s===u&&(a=2/3+e-t),
0>a?a+=1:a>1&&(a-=1)),[360*a,100*o,100*u];
},o.rgb.hwb=function(r){
var t=r[0],e=r[1],n=r[2],a=o.rgb.hsl(r)[0],i=1/255*Math.min(t,Math.min(e,n));
return n=1-1/255*Math.max(t,Math.max(e,n)),[a,100*i,100*n];
},o.rgb.cmyk=function(r){
var t,e,n,a,o=r[0]/255,i=r[1]/255,l=r[2]/255;
return a=Math.min(1-o,1-i,1-l),t=(1-o-a)/(1-a)||0,e=(1-i-a)/(1-a)||0,n=(1-l-a)/(1-a)||0,
[100*t,100*e,100*n,100*a];
},o.rgb.keyword=function(r){
var a=n[r];
if(a)return a;
var o,i=1/0;
for(var l in e)if(e.hasOwnProperty(l)){
var s=e[l],u=t(r,s);
i>u&&(i=u,o=l);
}
return o;
},o.keyword.rgb=function(r){
return e[r];
},o.rgb.xyz=function(r){
var t=r[0]/255,e=r[1]/255,n=r[2]/255;
t=t>.04045?Math.pow((t+.055)/1.055,2.4):t/12.92,e=e>.04045?Math.pow((e+.055)/1.055,2.4):e/12.92,
n=n>.04045?Math.pow((n+.055)/1.055,2.4):n/12.92;
var a=.4124*t+.3576*e+.1805*n,o=.2126*t+.7152*e+.0722*n,i=.0193*t+.1192*e+.9505*n;
return[100*a,100*o,100*i];
},o.rgb.lab=function(r){
var t,e,n,a=o.rgb.xyz(r),i=a[0],l=a[1],s=a[2];
return i/=95.047,l/=100,s/=108.883,i=i>.008856?Math.pow(i,1/3):7.787*i+16/116,l=l>.008856?Math.pow(l,1/3):7.787*l+16/116,
s=s>.008856?Math.pow(s,1/3):7.787*s+16/116,t=116*l-16,e=500*(i-l),n=200*(l-s),[t,e,n];
},o.hsl.rgb=function(r){
var t,e,n,a,o,i=r[0]/360,l=r[1]/100,s=r[2]/100;
if(0===l)return o=255*s,[o,o,o];
e=.5>s?s*(1+l):s+l-s*l,t=2*s-e,a=[0,0,0];
for(var u=0;3>u;u++)n=i+1/3*-(u-1),0>n&&n++,n>1&&n--,o=1>6*n?t+6*(e-t)*n:1>2*n?e:2>3*n?t+(e-t)*(2/3-n)*6:t,
a[u]=255*o;
return a;
},o.hsl.hsv=function(r){
var t,e,n=r[0],a=r[1]/100,o=r[2]/100,i=a,l=Math.max(o,.01);
return o*=2,a*=1>=o?o:2-o,i*=1>=l?l:2-l,e=(o+a)/2,t=0===o?2*i/(l+i):2*a/(o+a),[n,100*t,100*e];
},o.hsv.rgb=function(r){
var t=r[0]/60,e=r[1]/100,n=r[2]/100,a=Math.floor(t)%6,o=t-Math.floor(t),i=255*n*(1-e),l=255*n*(1-e*o),s=255*n*(1-e*(1-o));
switch(n*=255,a){
case 0:
return[n,s,i];

case 1:
return[l,n,i];

case 2:
return[i,n,s];

case 3:
return[i,l,n];

case 4:
return[s,i,n];

case 5:
return[n,i,l];
}
},o.hsv.hsl=function(r){
var t,e,n,a=r[0],o=r[1]/100,i=r[2]/100,l=Math.max(i,.01);
return n=(2-o)*i,t=(2-o)*l,e=o*l,e/=1>=t?t:2-t,e=e||0,n/=2,[a,100*e,100*n];
},o.hwb.rgb=function(r){
var t,e,n,a,o=r[0]/360,i=r[1]/100,l=r[2]/100,s=i+l;
s>1&&(i/=s,l/=s),t=Math.floor(6*o),e=1-l,n=6*o-t,0!==(1&t)&&(n=1-n),a=i+n*(e-i);
var u,c,h;
switch(t){
default:
case 6:
case 0:
u=e,c=a,h=i;
break;

case 1:
u=a,c=e,h=i;
break;

case 2:
u=i,c=e,h=a;
break;

case 3:
u=i,c=a,h=e;
break;

case 4:
u=a,c=i,h=e;
break;

case 5:
u=e,c=i,h=a;
}
return[255*u,255*c,255*h];
},o.cmyk.rgb=function(r){
var t,e,n,a=r[0]/100,o=r[1]/100,i=r[2]/100,l=r[3]/100;
return t=1-Math.min(1,a*(1-l)+l),e=1-Math.min(1,o*(1-l)+l),n=1-Math.min(1,i*(1-l)+l),
[255*t,255*e,255*n];
},o.xyz.rgb=function(r){
var t,e,n,a=r[0]/100,o=r[1]/100,i=r[2]/100;
return t=3.2406*a+-1.5372*o+i*-.4986,e=a*-.9689+1.8758*o+.0415*i,n=.0557*a+o*-.204+1.057*i,
t=t>.0031308?1.055*Math.pow(t,1/2.4)-.055:12.92*t,e=e>.0031308?1.055*Math.pow(e,1/2.4)-.055:12.92*e,
n=n>.0031308?1.055*Math.pow(n,1/2.4)-.055:12.92*n,t=Math.min(Math.max(0,t),1),e=Math.min(Math.max(0,e),1),
n=Math.min(Math.max(0,n),1),[255*t,255*e,255*n];
},o.xyz.lab=function(r){
var t,e,n,a=r[0],o=r[1],i=r[2];
return a/=95.047,o/=100,i/=108.883,a=a>.008856?Math.pow(a,1/3):7.787*a+16/116,o=o>.008856?Math.pow(o,1/3):7.787*o+16/116,
i=i>.008856?Math.pow(i,1/3):7.787*i+16/116,t=116*o-16,e=500*(a-o),n=200*(o-i),[t,e,n];
},o.lab.xyz=function(r){
var t,e,n,a=r[0],o=r[1],i=r[2];
e=(a+16)/116,t=o/500+e,n=e-i/200;
var l=Math.pow(e,3),s=Math.pow(t,3),u=Math.pow(n,3);
return e=l>.008856?l:(e-16/116)/7.787,t=s>.008856?s:(t-16/116)/7.787,n=u>.008856?u:(n-16/116)/7.787,
t*=95.047,e*=100,n*=108.883,[t,e,n];
},o.lab.lch=function(r){
var t,e,n,a=r[0],o=r[1],i=r[2];
return t=Math.atan2(i,o),e=360*t/2/Math.PI,0>e&&(e+=360),n=Math.sqrt(o*o+i*i),[a,n,e];
},o.lch.lab=function(r){
var t,e,n,a=r[0],o=r[1],i=r[2];
return n=i/360*2*Math.PI,t=o*Math.cos(n),e=o*Math.sin(n),[a,t,e];
},o.rgb.ansi16=function(r){
var t=r[0],e=r[1],n=r[2],a=1 in arguments?arguments[1]:o.rgb.hsv(r)[2];
if(a=Math.round(a/50),0===a)return 30;
var i=30+(Math.round(n/255)<<2|Math.round(e/255)<<1|Math.round(t/255));
return 2===a&&(i+=60),i;
},o.hsv.ansi16=function(r){
return o.rgb.ansi16(o.hsv.rgb(r),r[2]);
},o.rgb.ansi256=function(r){
var t=r[0],e=r[1],n=r[2];
if(t===e&&e===n)return 8>t?16:t>248?231:Math.round((t-8)/247*24)+232;
var a=16+36*Math.round(t/255*5)+6*Math.round(e/255*5)+Math.round(n/255*5);
return a;
},o.ansi16.rgb=function(r){
var t=r%10;
if(0===t||7===t)return r>50&&(t+=3.5),t=t/10.5*255,[t,t,t];
var e=.5*(~~(r>50)+1),n=(1&t)*e*255,a=(t>>1&1)*e*255,o=(t>>2&1)*e*255;
return[n,a,o];
},o.ansi256.rgb=function(r){
if(r>=232){
var t=10*(r-232)+8;
return[t,t,t];
}
r-=16;
var e,n=Math.floor(r/36)/5*255,a=Math.floor((e=r%36)/6)/5*255,o=e%6/5*255;
return[n,a,o];
},o.rgb.hex=function(r){
var t=((255&Math.round(r[0]))<<16)+((255&Math.round(r[1]))<<8)+(255&Math.round(r[2])),e=t.toString(16).toUpperCase();
return"000000".substring(e.length)+e;
},o.hex.rgb=function(r){
var t=r.toString(16).match(/[a-f0-9]{6}|[a-f0-9]{3}/i);
if(!t)return[0,0,0];
var e=t[0];
3===t[0].length&&(e=e.split("").map(function(r){
return r+r;
}).join(""));
var n=parseInt(e,16),a=n>>16&255,o=n>>8&255,i=255&n;
return[a,o,i];
},o.rgb.hcg=function(r){
var t,e,n=r[0]/255,a=r[1]/255,o=r[2]/255,i=Math.max(Math.max(n,a),o),l=Math.min(Math.min(n,a),o),s=i-l;
return t=1>s?l/(1-s):0,e=0>=s?0:i===n?(a-o)/s%6:i===a?2+(o-n)/s:4+(n-a)/s+4,e/=6,
e%=1,[360*e,100*s,100*t];
},o.hsl.hcg=function(r){
var t=r[1]/100,e=r[2]/100,n=1,a=0;
return n=.5>e?2*t*e:2*t*(1-e),1>n&&(a=(e-.5*n)/(1-n)),[r[0],100*n,100*a];
},o.hsv.hcg=function(r){
var t=r[1]/100,e=r[2]/100,n=t*e,a=0;
return 1>n&&(a=(e-n)/(1-n)),[r[0],100*n,100*a];
},o.hcg.rgb=function(r){
var t=r[0]/360,e=r[1]/100,n=r[2]/100;
if(0===e)return[255*n,255*n,255*n];
var a=[0,0,0],o=t%1*6,i=o%1,l=1-i,s=0;
switch(Math.floor(o)){
case 0:
a[0]=1,a[1]=i,a[2]=0;
break;

case 1:
a[0]=l,a[1]=1,a[2]=0;
break;

case 2:
a[0]=0,a[1]=1,a[2]=i;
break;

case 3:
a[0]=0,a[1]=l,a[2]=1;
break;

case 4:
a[0]=i,a[1]=0,a[2]=1;
break;

default:
a[0]=1,a[1]=0,a[2]=l;
}
return s=(1-e)*n,[255*(e*a[0]+s),255*(e*a[1]+s),255*(e*a[2]+s)];
},o.hcg.hsv=function(r){
var t=r[1]/100,e=r[2]/100,n=t+e*(1-t),a=0;
return n>0&&(a=t/n),[r[0],100*a,100*n];
},o.hcg.hsl=function(r){
var t=r[1]/100,e=r[2]/100,n=e*(1-t)+.5*t,a=0;
return n>0&&.5>n?a=t/(2*n):n>=.5&&1>n&&(a=t/(2*(1-n))),[r[0],100*a,100*n];
},o.hcg.hwb=function(r){
var t=r[1]/100,e=r[2]/100,n=t+e*(1-t);
return[r[0],100*(n-t),100*(1-n)];
},o.hwb.hcg=function(r){
var t=r[1]/100,e=r[2]/100,n=1-e,a=n-t,o=0;
return 1>a&&(o=(n-a)/(1-a)),[r[0],100*a,100*o];
},o.apple.rgb=function(r){
return[r[0]/65535*255,r[1]/65535*255,r[2]/65535*255];
},o.rgb.apple=function(r){
return[r[0]/255*65535,r[1]/255*65535,r[2]/255*65535];
},o.gray.rgb=function(r){
return[r[0]/100*255,r[0]/100*255,r[0]/100*255];
},o.gray.hsl=o.gray.hsv=function(r){
return[0,0,r[0]];
},o.gray.hwb=function(r){
return[0,100,r[0]];
},o.gray.cmyk=function(r){
return[0,0,0,r[0]];
},o.gray.lab=function(r){
return[r[0],0,0];
},o.gray.hex=function(r){
var t=255&Math.round(r[0]/100*255),e=(t<<16)+(t<<8)+t,n=e.toString(16).toUpperCase();
return"000000".substring(n.length)+n;
},o.rgb.gray=function(r){
var t=(r[0]+r[1]+r[2])/3;
return[t/255*100];
},o;
}(),a=function(){
function r(){
for(var r={},t=Object.keys(o),e=t.length,n=0;e>n;n++)r[t[n]]={
distance:-1,
parent:null
};
return r;
}
function t(t){
var e=r(),n=[t];
for(e[t].distance=0;n.length;)for(var a=n.pop(),i=Object.keys(o[a]),l=i.length,s=0;l>s;s++){
var u=i[s],c=e[u];
-1===c.distance&&(c.distance=e[a].distance+1,c.parent=a,n.unshift(u));
}
return e;
}
function e(r,t){
return function(e){
return t(r(e));
};
}
function a(r,t){
for(var n=[t[r].parent,r],a=o[t[r].parent][r],i=t[r].parent;t[i].parent;)n.unshift(t[i].parent),
a=e(o[t[i].parent][i],a),i=t[i].parent;
return a.conversion=n,a;
}
var o=n;
return function(r){
for(var e=t(r),n={},o=Object.keys(e),i=o.length,l=0;i>l;l++){
var s=o[l],u=e[s];
null!==u.parent&&(n[s]=a(s,e));
}
return n;
};
}(),o={},i=Object.keys(n);
return i.forEach(function(r){
o[r]={},Object.defineProperty(o[r],"channels",{
value:n[r].channels
}),Object.defineProperty(o[r],"labels",{
value:n[r].labels
});
var i=a(r),l=Object.keys(i);
l.forEach(function(n){
var a=i[n];
o[r][n]=e(a),o[r][n].raw=t(a);
});
}),o;
}(),c=[].slice,h=["keyword","gray","hex"],f={};
Object.keys(u).forEach(function(r){
f[c.call(u[r].labels).sort().join("")]=r;
});
var g={};
return t.prototype={
toString:function(){
return this.string();
},
toJSON:function(){
return this[this.model]();
},
string:function(r){
var t=this.model in s.to?this:this.rgb();
t=t.round("number"==typeof r?r:1);
var e=1===t.valpha?t.color:t.color.concat(this.valpha);
return s.to[t.model](e);
},
percentString:function(r){
var t=this.rgb().round("number"==typeof r?r:1),e=1===t.valpha?t.color:t.color.concat(this.valpha);
return s.to.rgb.percent(e);
},
array:function(){
return 1===this.valpha?this.color.slice():this.color.concat(this.valpha);
},
object:function(){
for(var r={},t=u[this.model].channels,e=u[this.model].labels,n=0;t>n;n++)r[e[n]]=this.color[n];
return 1!==this.valpha&&(r.alpha=this.valpha),r;
},
unitArray:function(){
var r=this.rgb().color;
return r[0]/=255,r[1]/=255,r[2]/=255,1!==this.valpha&&r.push(this.valpha),r;
},
unitObject:function(){
var r=this.rgb().object();
return r.r/=255,r.g/=255,r.b/=255,1!==this.valpha&&(r.alpha=this.valpha),r;
},
round:function(r){
return r=Math.max(r||0,0),new t(this.color.map(n(r)).concat(this.valpha),this.model);
},
alpha:function(r){
return arguments.length?new t(this.color.concat(Math.max(0,Math.min(1,r))),this.model):this.valpha;
},
red:a("rgb",0,o(255)),
green:a("rgb",1,o(255)),
blue:a("rgb",2,o(255)),
hue:a(["hsl","hsv","hsl","hwb","hcg"],0,function(r){
return(r%360+360)%360;
}),
saturationl:a("hsl",1,o(100)),
lightness:a("hsl",2,o(100)),
saturationv:a("hsv",1,o(100)),
value:a("hsv",2,o(100)),
chroma:a("hcg",1,o(100)),
gray:a("hcg",2,o(100)),
white:a("hwb",1,o(100)),
wblack:a("hwb",2,o(100)),
cyan:a("cmyk",0,o(100)),
magenta:a("cmyk",1,o(100)),
yellow:a("cmyk",2,o(100)),
black:a("cmyk",3,o(100)),
x:a("xyz",0,o(100)),
y:a("xyz",1,o(100)),
z:a("xyz",2,o(100)),
l:a("lab",0,o(100)),
a:a("lab",1),
b:a("lab",2),
keyword:function(r){
return arguments.length?new t(r):u[this.model].keyword(this.color);
},
hex:function(r){
return arguments.length?new t(r):s.to.hex(this.rgb().round().color);
},
rgbNumber:function(){
var r=this.rgb().color;
return(255&r[0])<<16|(255&r[1])<<8|255&r[2];
},
luminosity:function(){
for(var r=this.rgb().color,t=[],e=0;e<r.length;e++){
var n=r[e]/255;
t[e]=.03928>=n?n/12.92:Math.pow((n+.055)/1.055,2.4);
}
return.2126*t[0]+.7152*t[1]+.0722*t[2];
},
contrast:function(r){
var t=this.luminosity(),e=r.luminosity();
return t>e?(t+.05)/(e+.05):(e+.05)/(t+.05);
},
level:function(r){
var t=this.contrast(r);
return t>=7.1?"AAA":t>=4.5?"AA":"";
},
isDark:function(){
var r=this.rgb().color,t=(299*r[0]+587*r[1]+114*r[2])/1e3;
return 128>t;
},
isLight:function(){
return!this.isDark();
},
negate:function(){
for(var r=this.rgb(),t=0;3>t;t++)r.color[t]=255-r.color[t];
return r;
},
lighten:function(r){
var t=this.hsl();
return t.color[2]+=t.color[2]*r,t;
},
darken:function(r){
var t=this.hsl();
return t.color[2]-=t.color[2]*r,t;
},
saturate:function(r){
var t=this.hsl();
return t.color[1]+=t.color[1]*r,t;
},
desaturate:function(r){
var t=this.hsl();
return t.color[1]-=t.color[1]*r,t;
},
whiten:function(r){
var t=this.hwb();
return t.color[1]+=t.color[1]*r,t;
},
blacken:function(r){
var t=this.hwb();
return t.color[2]+=t.color[2]*r,t;
},
grayscale:function(){
var r=this.rgb().color,e=.3*r[0]+.59*r[1]+.11*r[2];
return t.rgb(e,e,e);
},
fade:function(r){
return this.alpha(this.valpha-this.valpha*r);
},
opaquer:function(r){
return this.alpha(this.valpha+this.valpha*r);
},
rotate:function(r){
var t=this.hsl(),e=t.color[0];
return e=(e+r)%360,e=0>e?360+e:e,t.color[0]=e,t;
},
mix:function(r,e){
if(!r||!r.rgb)throw new Error('Argument to "mix" was not a Color instance, but rather an instance of '+("undefined"==typeof r?"undefined":_typeof(r)));
var n=r.rgb(),a=this.rgb(),o=void 0===e?.5:e,i=2*o-1,l=n.alpha()-a.alpha(),s=((i*l===-1?i:(i+l)/(1+i*l))+1)/2,u=1-s;
return t.rgb(s*n.red()+u*a.red(),s*n.green()+u*a.green(),s*n.blue()+u*a.blue(),n.alpha()*o+a.alpha()*(1-o));
}
},Object.keys(u).forEach(function(r){
if(-1===h.indexOf(r)){
var e=u[r].channels;
t.prototype[r]=function(){
if(this.model===r)return new t(this);
if(arguments.length)return new t(arguments,r);
var n="number"==typeof arguments[e]?e:this.valpha;
return new t(i(u[this.model][r].raw(this.color)).concat(n),r);
},t[r]=function(n){
return"number"==typeof n&&(n=l(c.call(arguments),e)),new t(n,r);
};
}
}),t;
}(),e=new RegExp(Object.keys(r).join("|"),"ig"),n="#666",a="data-darkmode-color",o="data-darkmode-bgcolor",i="data-darkmode-bgimage",l=window.dmClassPrefix,s=window.getInnerHeight&&window.getInnerHeight()||window.innerHeight||document.documentElement.clientHeight,u=navigator.userAgent,c=/(iPhone|iPad|iPod|iOS)/i.test(u),h=/mac\sos/i.test(u),f=/windows\snt/i.test(u)&&!/Windows\sPhone/i.test(u),g=0,b=[],d=[],v=["mpcps","iframe"],p=[],m=[],y=["",""],w=!0,M=function(r,t){
return r+": "+t+" !important;";
},k=function(r){
var t;
return(t=[r]).concat.apply(t,_toConsumableArray(r.querySelectorAll("*")));
},x=function(r,e,n){
var a=r.rgb().array(),l=r.hsl().array(),s=r.alpha(),u=(299*a[0]+587*a[1]+114*a[2])/1e3,c=250,h=190,f=void 0;
if(n.isBgColor)if(0===l[1]&&l[2]>40||u>c)f=t.hsl(0,0,Math.min(100,114-l[2]));else if(u>h){
var g=1e3*h/(299*a[0]+587*a[1]+114*a[2]);
f=t.rgb(a[0]*g,a[1]*g,a[2]*g);
}else l[2]<26&&(l[2]=26,f=t.hsl.apply(t,_toConsumableArray(l)));else if(n.isTextColor||n.isBorderColor){
var b=!1,d=e.getAttribute(o);
if(!e.getAttribute(i)){
if(d){
var v=t(d).rgb().array();
b=(299*v[0]+587*v[1]+114*v[2])/1e3>h-20;
}
(!b&&l[2]<40||b&&c>u&&u>=h)&&(l[2]=90-l[2],f=t.hsl.apply(t,_toConsumableArray(l)));
}
}
return f&&f.alpha(s).rgb();
},A=function(s){
if(v.indexOf(s.nodeName.toLowerCase())>-1||Array.prototype.some.call(s.classList,function(r){
return b.indexOf(r)>-1||d.some(function(t){
return t.test(r);
});
}))return"";
var u=s.style,p="";
try{
!function(){
var l=!1;
(u.cssText&&u.cssText.split(";")||[]).map(function(r){
var t=r.indexOf(":");
return[r.slice(0,t).toLowerCase(),r.slice(t+1)].map(function(r){
return(r||"").replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,"");
});
}).filter(function(r){
var t=_slicedToArray(r,1),e=t[0];
return["-webkit-border-image","border-image","color","background-color","background-image","background","border","border-top","border-right","border-bottom","border-left","border-color","border-top-color","border-right-color","border-bottom-color","border-left-color"].indexOf(e)>-1;
}).sort(function(r){
var t=_slicedToArray(r,1),e=t[0];
return"color"===e?(l=!0,0):-1;
}).forEach(function(u){
var c=_slicedToArray(u,2),h=c[0],f=c[1],g=!1;
f=f.replace(e,function(t){
return"rgb("+r[t.toLowerCase()].toString()+")";
});
var b=/rgba?\([^)]+\)/gi;
b.test(f)&&!function(){
var r=!1;
f=f.replace(b,function(e){
var n=/^background/.test(h),l="color"===h,u=/^border/.test(h),c=x(t(e),s,{
isBgColor:n,
isTextColor:l,
isBorderColor:u
});
return c&&!r&&(n||l)&&!function(){
r=!0;
var t=n?o:a,e=c.toString();
k(s).forEach(function(r){
r.setAttribute(t,e),n&&r.getAttribute(i)&&r.removeAttribute(i);
});
}(),c&&(g=!0),c||e;
}).replace(/\s?!\s?important/gi,"");
}();
var d=.15;
(/^background/.test(h)||/^(-webkit-)?border-image/.test(h))&&/url\([^\)]*\)/i.test(f)&&(g=!0,
f=f.replace(/^(.*?)url\(([^\)]*)\)(.*)$/i,function(r,t,e,n){
return"1"!==s.getAttribute(i)&&k(s).forEach(function(r){
return r.setAttribute(i,"1");
}),t+"linear-gradient(rgba(0, 0, 0, "+d+"), rgba(0, 0, 0, "+d+")), url("+e+")"+n;
}),!s.getAttribute(a)&&!l&&(p+=M("color",n))),g&&(p+=M(h,f));
});
}();
}catch(m){
console.error(m);
}
if(p){
(f||h&&!c)&&s.setAttribute("data-style",u.cssText);
var y=""+l+g++;
return s.classList.add(y),"."+y+"{"+p+"}";
}
return"";
},O=function(r){
null!==y&&(r?p.forEach(function(r){
if(w){
var t=r.getBoundingClientRect(),e=t.top,n=t.bottom;
0>=e&&0>=n?y[1]+=A(r):e>0&&s>e||n>0&&s>n?(m.push(r),y[0]+=A(r)):(w=!1,y[0]&&document.head.insertAdjacentHTML("beforeend",'<style type="text/css">@media (prefers-color-scheme: dark) {'+y[0]+"}</style>"),
m.forEach(function(r){
r.style.visibility="visible";
}),y[0]="",y[1]+=A(r));
}else y[1]+=A(r);
}):w=!1,y[1]=y[0]+y[1],y[1]&&(document.head.insertAdjacentHTML("beforeend",'<style type="text/css">@media (prefers-color-scheme: dark) {'+y[1]+"}</style>"),
y=null,p=null,m=null));
},j=window.matchMedia("(prefers-color-scheme: dark)"),C=function(r){
var t=r.matches;
return O(t);
};
return j.addListener(C),function(r){
p=r.nodes||[],b=b.concat(r.whiteListClass||[]),d=d.concat(r.whiteListClassReg||[]),
v=v.concat(r.whiteListName||[]),C(j),document.getElementById("js_content").style.visibility="visible";
};
});
</script>

<script nonce="567503264" type="text/javascript">
    var new_appmsg = 1;
    var item_show_type = "0";
    var can_see_complaint = "0";
    var not_in_mm_css = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/style/page/appmsg_new/not_in_mm492bcc.css";
    var windowwx_css = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/style/page/appmsg_new/winwx492bcc.css";
    var article_improve_combo_css = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/style/page/appmsg_new/combo4af382.css";
    var tid = "";
    var aid = "";
    var clientversion = "";
    var appuin = "MjM5NDg5MjExMQ=="||"";

    var source = "";
    var ascene = "";
    var subscene = "";
    var sessionid = ""||"svr_664a014fd88";
    var abtest_cookie = "";

    var scene = 75;

    var itemidx = "";
    var appmsg_token   = "";
    var _copyright_stat = "0";
    var _ori_article_type = "";

    var is_follow = "";
    var nickname = "中国青年网";
    var nickname_new = "";
    var appmsg_type = "9";
    var ct = "1578198176";
    var user_name = "gh_57c55c6408be";
    var user_name_new = "";
    var fakeid   = "";
    var version   = "";
    var is_limit_user   = "0";
    var round_head_img = "http://mmbiz.qpic.cn/mmbiz_png/YADYBggmmQTbVMcdviaA97g0OxUNu61k0UrqNQtiaO0XXIcYxhwSLDAiaib0MTPKkJnNKbZfMAv99BmiajDeDiaibw4qQ/0?wx_fmt=png";
    var hd_head_img = "http://wx.qlogo.cn/mmhead/Q3auHgzwzM6cymZN02pef7gaGiamjn1xBiaFKePibff4NJad3CODrY6oQ/0"||"";
    var ori_head_img_url = "http://wx.qlogo.cn/mmhead/Q3auHgzwzM6cymZN02pef7gaGiamjn1xBiaFKePibff4NJad3CODrY6oQ/132";
    var msg_title = "这名99后跳下冰河冻得呻吟发抖，他却说......";
    var msg_desc = "";
    var msg_cdn_url = "http://mmbiz.qpic.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdk53oez8Pp9VkYy0xF8GxicvW0XDZBvsakC8qgyAXD8aFVTy868wRNJ9A/0?wx_fmt=jpeg"; 
    var cdn_url_1_1  = "https://mmbiz.qlogo.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdkgGnsAUvwZGdp0EboVUrs3h88Zib17EiboGR3G8hFqGoiayfHQJRA2tTCA/0?wx_fmt=jpeg"; 
    var cdn_url_235_1 = "https://mmbiz.qlogo.cn/mmbiz_jpg/YADYBggmmQS8zAImlibnpXAxxiaRKxeTdk53oez8Pp9VkYy0xF8GxicvW0XDZBvsakC8qgyAXD8aFVTy868wRNJ9A/0?wx_fmt=jpeg"; 
    
    var msg_link = "http://mp.weixin.qq.com/s?__biz=MjM5NDg5MjExMQ==&amp;mid=2650775174&amp;idx=1&amp;sn=763df4247d40384132e0a6b5361275a5&amp;chksm=be8beea689fc67b0c2feaa4223410378b28c0f1d3ee99c033c89d499ce2c205e4c07a3b95224#rd"; 
    var user_uin = ""*1;
    var msg_source_url = '';
    var img_format = 'jpeg';
    var srcid = '';
    var req_id = '0911HRkMULuEV22Z24tiI4CF';
    var networkType;
    var appmsgid = '' || '2650775174'|| "";
    var comment_id = "1151016092245180416" || "1151016092245180416" * 1;
    var comment_enabled = "" * 1;
    var is_need_reward = '0' * 1 ? 0 : "0" * 1; 
    var is_https_res = ("" * 1) && (location.protocol == "https:");
    var msg_daily_idx = "1" || "";
    var profileReportInfo = "" || "";

    var devicetype = "";
    var source_encode_biz = ""; 
    var source_username = "";
    
    var reprint_ticket = "";
    var source_mid = "";
    var source_idx = "";
    var source_biz = "";
    var author_id = "";

    
    var optimizing_flag = "0" * 1;

    
    

    var show_comment = "";
    var __appmsgCgiData = {
        wxa_product : ""*1,
        wxa_cps : ""*1,
        show_msg_voice: "0"*1,
        can_use_page : ""*1,
        is_wxg_stuff_uin : "0"*1,
        card_pos : "",
        copyright_stat : "0",
        source_biz : "",
        hd_head_img : "http://wx.qlogo.cn/mmhead/Q3auHgzwzM6cymZN02pef7gaGiamjn1xBiaFKePibff4NJad3CODrY6oQ/0"||(window.location.protocol+"//"+window.location.host + "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/pic/appmsg/pic_rumor_link.2x42f400.jpg")
    };
    var _empty_v = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/pic/pages/voice/empty42f400.mp3";

    var copyright_stat = "0" * 1;
    var hideSource = "" * 1;

    var pay_fee = "" * 1;
    var pay_timestamp = "";
    var need_pay = "" * 1;

    var need_report_cost = "0" * 1;
    var use_tx_video_player = "0" * 1;
    var appmsg_fe_filter = "contenteditable";

    var friend_read_source = "" || "";
    var friend_read_version = "" || "";
    var friend_read_class_id = "" || "";

    var is_only_read = "1" * 1;
    var read_num = "" * 1;
    var like_num = "" * 1;
    var liked = "" == 'true' ? true : false;
    var is_temp_url = "" ? 1 : 0;
    var send_time = "";
    var icon_emotion_switch = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg/emotion/icon_emotion_switch46b604.svg";
    var icon_emotion_switch_active = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg/emotion/icon_emotion_switch_active46b604.svg";
    var icon_emotion_switch_primary = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg/emotion/icon_emotion_switch_primary46b604.svg";
    var icon_emotion_switch_active_primary = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg/emotion/icon_emotion_switch_active_primary46b604.svg";
    var icon_loading_white = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/common/icon_loading_white42f400.gif";
    var icon_audio_unread = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg/audio/icon_audio_unread42f400.png";
    var icon_qqmusic_default = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg/qqmusic/icon_qqmusic_default.2x42f400.png";
    var icon_qqmusic_source = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg/qqmusic/icon_qqmusic_source4abca9.svg";
    var icon_kugou_source = "//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg/kugou/icon_kugou_source42f400.png";

    var topic_default_img = '//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg/topic/pic_book_thumb.2x42f400.png';
    var comment_edit_icon = '//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/appmsg_new/icon_edit42f400.png';
    var comment_loading_img = '//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/icon/common/icon_loading_white42f400.gif';

    var voice_in_appmsg = {
        "1":"1"
            };

    var reprint_style = ''*1;
    var wxa_img_alert = "" != 'false';

    
    var img_popup = 1; 

    
    var more_read_type = '0'*1;

    
    
    
    

    
    var weapp_sn_arr_json = "" || "";

    
    var ban_scene = "0" * 1;

    var svr_time = "1578540388" * 1;
    
    var is_transfer_msg = ""*1||0;

    var malicious_title_reason_id = "0" * 1; 
    var malicious_content_type = "0" * 1; 

    
    var modify_time = "";

    
    var isprofileblock = "0";

    
    var hotspotInfoList = [
                    ];

    var jumpInfo = [
                    ];

    var hasRelatedArticleInfo = '0' * 1 || 0; 

        window.wxtoken = "777";
        
    
    
    
    
    window.is_login = '' * 1; 

    window.__moon_initcallback = function(){
        if(!!window.__initCatch){
            window.__initCatch({
                idkey : 27611+2,
                startKey : 0,
                limit : 128,
                badjsId: 43,
                reportOpt : {
                    uin : uin,
                    biz : biz,
                    mid : mid,
                    idx : idx,
                    sn  : sn
                },
                extInfo : {
                    network_rate : 0.01,    
                    badjs_rate: 0.1 
                }
            });
        }
    }
        
    var title ="中国青年网";

    var is_new_msg=true;
    
    

    var is_wash = '' * 1;
    var topbarEnable = false;
    var enterid = "" * 1 || "" * 1 || 0;
    var appid_list = ""; 

    var defaultAvatarUrl = '//res.wx.qq.com/mmbizwap/zh_CN/htmledition/images/pic/common/avatar_default46e3e2.svg';

    document.addEventListener('DOMContentLoaded', function () {
        window.domCompleteTime = Date.now();
    });

    
                        var hasRecommendMsg = 0;
        ;
        
    var isPaySubscribe = '0' * 1; 
    var isPaid = '0' * 1; 
    var previewPercent = '0' || ''; 
    var is_finished_preview = 0; 
    var jump2pay = '' * 1; 
</script>

<script nonce="567503264" type="text/javascript">
(function(_g){
    _g.appmsg_like_type = "2" * 1 ? "2" * 1 : 1;
    
    _g.clientversion = "";
    _g.passparam = ""; 
    if(!_g.msg_link) {
      _g.msg_link = "http://mp.weixin.qq.com/s?__biz=MjM5NDg5MjExMQ==&amp;mid=2650775174&amp;idx=1&amp;sn=763df4247d40384132e0a6b5361275a5&amp;chksm=be8beea689fc67b0c2feaa4223410378b28c0f1d3ee99c033c89d499ce2c205e4c07a3b95224#rd";
    }
    _g.appmsg_type = "9"; 
    _g.devicetype = ""; 
})(window);

</script>


        <script nonce="567503264">window.__moon_host = 'res.wx.qq.com';window.__moon_mainjs = 'appmsg/index.js';window.moon_map = {"new_video/plugin/util.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/new_video/plugin/util4a091e.js","pages/iframe_communicate.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/iframe_communicate4848aa.js","new_video/player.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/new_video/player.html4af382.js","biz_wap/zepto/touch.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/zepto/touch42f400.js","biz_wap/zepto/event.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/zepto/event42f400.js","biz_wap/zepto/zepto.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/zepto/zepto440203.js","page/pages/video.css":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/style/page/pages/video.css4af382.js","a/tpl/smallbanner_msg_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/smallbanner_msg_tpl.html42f400.js","a/tpl/smallbanner_info_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/smallbanner_info_tpl.html44c2e3.js","a/tpl/banner_info_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/banner_info_tpl.html42f400.js","a/tpl/promote_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/promote_tpl.html42f400.js","a/tpl/smallcard_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/smallcard_tpl.html42f400.js","a/tpl/info_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/info_tpl.html42f400.js","a/tpl/cardticket_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/cardticket_tpl.html42f400.js","a/tpl/banner_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/banner_tpl.html47af5b.js","a/tpl/sponsor_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/sponsor_tpl.html42f400.js","a/tpl/new_cpc_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/new_cpc_tpl.html45178d.js","appmsg/emotion/caret.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/emotion/caret42f400.js","biz_wap/utils/localstorage.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/localstorage42f400.js","a/appdialog_confirm.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/appdialog_confirm.html42f400.js","widget/wx_profile_dialog_primary.css":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/style/widget/wx_profile_dialog_primary.css42f400.js","new_video/player.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/new_video/player4af5e8.js","a/tpl/mpda_bottom_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/mpda_bottom_tpl.html450c68.js","a/tpl/crt_size_map.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/crt_size_map4602fc.js","biz_wap/jsapi/cardticket.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/jsapi/cardticket42f400.js","pages/audition_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/audition_tpl.html47a8e6.js","biz_common/utils/emoji_panel_data.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/utils/emoji_panel_data42f400.js","appmsg/emotion/textarea.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/emotion/textarea42f400.js","appmsg/emotion/nav.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/emotion/nav42f400.js","appmsg/emotion/common.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/emotion/common42f400.js","appmsg/emotion/slide.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/emotion/slide49f7d6.js","biz_common/utils/emoji_data.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/utils/emoji_data45112f.js","pages/musicUrlReport.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/musicUrlReport47f34b.js","biz_wap/jsapi/log.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/jsapi/log4673d5.js","pages/music_report_conf.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/music_report_conf42f400.js","pages/report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/report4a2c10.js","pages/player_adaptor.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/player_adaptor42f400.js","pages/music_player.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/music_player473e5d.js","appmsg/more_read_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/more_read_tpl.html42f400.js","appmsg/friend_comment_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/friend_comment_tpl.html42f400.js","appmsg/comment_pc_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/comment_pc_tpl.html4830e1.js","appmsg/comment_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/comment_tpl.html4a2c3f.js","appmsg/emotion/emotion_pc.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/emotion/emotion_pc4a091e.js","appmsg/emotion/dom.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/emotion/dom42f400.js","biz_wap/utils/fakehash.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/fakehash42f400.js","appmsg/emotion/selection.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/emotion/selection4830e1.js","appmsg/comment_report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/comment_report4690d8.js","appmsg/retry_ajax.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/retry_ajax451cc4.js","complain/tips.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/complain/tips42f400.js","appmsg/i18n.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/i18n4af382.js","appmsg/related_article_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/related_article_tpl.html4a789c.js","pages/loadscript.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/loadscript42f400.js","biz_wap/utils/ajax_load_js.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/ajax_load_js42f400.js","appmsg/reward_entry.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/reward_entry46ef12.js","a/ios.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/ios42f400.js","a/android.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/android457bcb.js","a/profile.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/profile455ab4.js","a/app_card.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/app_card485189.js","a/sponsor.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/sponsor4af382.js","a/tpl/cpc_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/cpc_tpl.html450c68.js","a/appdialog_confirm.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/appdialog_confirm471cb1.js","biz_common/dom/offset.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/dom/offset4690d8.js","a/video.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/video482376.js","a/tpl/crt_tpl_manager.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/tpl/crt_tpl_manager450d79.js","a/cpc_a_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/cpc_a_tpl.html485189.js","a/sponsor_a_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/sponsor_a_tpl.html42f400.js","a/a_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/a_tpl.html485189.js","a/mpshop.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/mpshop42f400.js","a/wxopen_card.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/wxopen_card42f400.js","a/card.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/card42f400.js","biz_wap/utils/position.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/position42f400.js","a/a_report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/a_report4402ec.js","biz_wap/utils/show_time.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/show_time4543c6.js","biz_common/utils/get_para_list.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/utils/get_para_list4b110f.js","biz_wap/utils/openUrl.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/openUrl4402ec.js","a/a_sign.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/a_sign452c49.js","pages/player_tips.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/player_tips47a8e6.js","appmsg/my_comment_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/my_comment_tpl.html4a41a2.js","appmsg/cmt_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/cmt_tpl.html4af382.js","sougou/a_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/sougou/a_tpl.html42f400.js","appmsg/emotion/emotion.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/emotion/emotion46b604.js","biz_common/utils/report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/utils/report42f400.js","appmsg/articleReport.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/articleReport42f400.js","appmsg/topic_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/topic_tpl.html42f400.js","pages/utils.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/utils4af382.js","question_answer/utils.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/question_answer/utils4abcaa.js","question_answer/appmsg_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/question_answer/appmsg_tpl.html4a2c10.js","pages/weapp_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/weapp_tpl.html4abcaa.js","biz_common/utils/monitor.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/utils/monitor42f400.js","pages/voice_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/voice_tpl.html4abcaa.js","pages/kugoumusic_ctrl.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/kugoumusic_ctrl47cb36.js","pages/qqmusic_ctrl.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/qqmusic_ctrl47cb36.js","pages/voice_component.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/voice_component4ab8ad.js","pages/qqmusic_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/qqmusic_tpl.html4abcaa.js","new_video/ctl.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/new_video/ctl4a46b1.js","biz_wap/jsapi/leaveReport.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/jsapi/leaveReport482a87.js","biz_wap/utils/hand_up_state.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/hand_up_state42f400.js","biz_wap/utils/storage.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/storage42f400.js","biz_common/utils/http.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/utils/http42f400.js","biz_common/utils/cookie.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/utils/cookie42f400.js","appmsg/open_url_with_webview.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/open_url_with_webview440203.js","appmsg/more_read.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/more_read4576f8.js","appmsg/comment.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/comment4b0b83.js","appmsg/like.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/like4af382.js","appmsg/related_article.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/related_article4a52fe.js","appmsg/share_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/share_tpl.html42f400.js","appmsg/appmsgext.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/appmsgext4ab744.js","appmsg/img_copyright_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/img_copyright_tpl.html42f400.js","pages/video_ctrl.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/video_ctrl42f400.js","pages/create_txv.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/create_txv42f400.js","appmsg/pay_read_utils.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/pay_read_utils4af382.js","appmsg/reward_utils.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/reward_utils4ab744.js","biz_common/ui/imgonepx.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/ui/imgonepx42f400.js","appmsg/malicious_wording.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/malicious_wording42f400.js","biz_common/jquery.md5.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/jquery.md542f400.js","biz_common/utils/comm_report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/utils/comm_report4a789c.js","tpl/appmsg/loading.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/tpl/appmsg/loading.html4ab744.js","biz_common/base64.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/base6442f400.js","biz_common/utils/wxgspeedsdk.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/utils/wxgspeedsdk42f400.js","pages/version4video.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/version4video4af382.js","a/a_config.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/a_config4b061e.js","a/a_utils.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/a_utils482376.js","a/a.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/a4b110f.js","rt/appmsg/getappmsgext.rt.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/rt/appmsg/getappmsgext.rt42f400.js","pages/video_communicate_adaptor.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/pages/video_communicate_adaptor4af382.js","biz_wap/utils/ajax_wx.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/ajax_wx4a2b2d.js","biz_common/utils/respTypes.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/utils/respTypes42f400.js","biz_wap/utils/log.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/log42f400.js","sougou/index.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/sougou/index42f400.js","biz_wap/safe/mutation_observer_report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/safe/mutation_observer_report42f400.js","appmsg/fereport.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/fereport438bee.js","appmsg/fereport_without_localstorage.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/fereport_without_localstorage438bee.js","appmsg/report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/report4765b8.js","appmsg/report_and_source.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/report_and_source450c68.js","appmsg/appmsg_copy_report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/appmsg_copy_report4ab744.js","appmsg/cdn_speed_report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/cdn_speed_report4765b8.js","appmsg/wxtopic.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/wxtopic42f400.js","question_answer/appmsg.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/question_answer/appmsg4a2c10.js","appmsg/weapp.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/weapp4a2c10.js","appmsg/weproduct.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/weproduct4576f8.js","appmsg/voicemsg.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/voicemsg42f400.js","appmsg/autoread.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/autoread42f400.js","appmsg/voice.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/voice4abcaa.js","appmsg/qqmusic.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/qqmusic47cb36.js","appmsg/iframe.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/iframe4af5e8.js","appmsg/page_pos.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/page_pos4ab744.js","appmsg/product.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/product4576f8.js","appmsg/review_image.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/review_image46a084.js","appmsg/outer_link.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/outer_link4a2b2d.js","appmsg/copyright_report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/copyright_report4a2c10.js","appmsg/async.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/async4b06cc.js","biz_wap/ui/lazyload_img.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/ui/lazyload_img42f400.js","biz_common/log/jserr.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/log/jserr42f400.js","appmsg/share.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/share475580.js","appmsg/cdn_img_lib.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/cdn_img_lib42f400.js","page/appmsg_new/not_in_mm.css":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/style/page/appmsg_new/not_in_mm.css492bcc.js","page/appmsg_new/combo.css":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/style/page/appmsg_new/combo.css4af382.js","common/comm_report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/common/comm_report49d6de.js","appmsg/finance_communicate.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/finance_communicate4a41a2.js","appmsg/loading.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/loading4af382.js","appmsg/pay_report_utils.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/pay_report_utils4ab744.js","appmsg/popup_report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/popup_report488f96.js","complain/localstorage.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/complain/localstorage42f400.js","common/utils.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/common/utils4af5e8.js","biz_wap/utils/wapsdk.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/wapsdk44c130.js","a/mpAdAsync.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/a/mpAdAsync4ac28f.js","biz_common/utils/url/parse.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/utils/url/parse440451.js","appmsg/appmsg_report.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/appmsg_report4ab744.js","biz_common/moment.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/moment42f400.js","biz_wap/jsapi/core.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/jsapi/core48ce4f.js","biz_common/dom/event.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/dom/event4b061e.js","appmsg/test.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/test42f400.js","biz_wap/utils/mmversion.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/mmversion45fc7f.js","appmsg/max_age.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/max_age42f400.js","biz_common/dom/attr.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/dom/attr42f400.js","biz_wap/utils/ajax.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/ajax4a2b2d.js","appmsg/log.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/log42f400.js","biz_common/dom/class.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/dom/class42f400.js","biz_wap/utils/device.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/utils/device4830e1.js","appmsg/weapp_common.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/weapp_common48ce4f.js","biz_common/utils/string/html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/utils/string/html42f400.js","cps/tpl/list_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/cps/tpl/list_tpl.html4abcaa.js","cps/tpl/card_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/cps/tpl/card_tpl.html4abcaa.js","cps/tpl/banner_tpl.html.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/cps/tpl/banner_tpl.html4abcaa.js","biz_common/tmpl.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_common/tmpl485189.js","appmsg/set_font_size.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/set_font_size499238.js","biz_wap/ui/weui.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/biz_wap/ui/weui4ab744.js","appmsg/index.js":"//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/appmsg/index4b110f.js"};</script><script nonce="567503264" type="text/javascript" id="moon_inline" > window.__mooninline=1; window.setTimeout(function() {  function __moonf__(){
if(!window.__moonhasinit){
window.__moonhasinit=!0,window.__moonclientlog=[],window.__wxgspeeds&&(window.__wxgspeeds.moonloadedtime=+new Date),
"object"!=typeof JSON&&(window.JSON={
stringify:function(){
return"";
},
parse:function(){
return{};
}
});
var e=function(){
function e(e){
try{
var o;
/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)?o="writeLog":/(Android)/i.test(navigator.userAgent)&&(o="log"),
o&&n(o,e);
}catch(t){
throw console.error(t),t;
}
}
function n(e,o){
var t,r,i={};
t=top!=window?top.window:window;
try{
r=t.WeixinJSBridge,i=t.document;
}catch(a){}
e&&r&&r.invoke?r.invoke(e,{
level:"info",
msg:"[WechatFe][moon]"+o
}):setTimeout(function(){
i.addEventListener?i.addEventListener("WeixinJSBridgeReady",function(){
n(e,o);
},!1):i.attachEvent&&(i.attachEvent("WeixinJSBridgeReady",function(){
n(e,o);
}),i.attachEvent("onWeixinJSBridgeReady",function(){
n(e,o);
}));
},0);
}
var t;
localStorage&&JSON.parse(localStorage.getItem("__WXLS__moonarg"))&&"fromls"==JSON.parse(localStorage.getItem("__WXLS__moonarg")).method&&(t=!0),
e(" moon init, moon_inline:"+window.__mooninline+", moonls:"+t),function(){
var e={},o={},n={};
e.COMBO_UNLOAD=0,e.COMBO_LOADING=1,e.COMBO_LOADED=2;
var t=function(e,n,t){
if(!o[e]){
o[e]=t;
for(var r=3;r--;)try{
moon.setItem(moon.prefix+e,t.toString()),moon.setItem(moon.prefix+e+"_ver",moon_map[e]);
break;
}catch(i){
moon.clear();
}
}
},r=window.alert;
window.__alertList=[],window.alert=function(e){
r(e),window.__alertList.push(e);
};
var i=function(e){
if(!e||!o[e])return null;
var t=o[e];
if("function"==typeof t&&!n[e]){
var a={},s={
exports:a
},c=t(i,a,s,r);
t=o[e]=c||s.exports,n[e]=!0;
}
if(".css"===e.substr(-4)){
var d=document.getElementById(e);
if(!d){
d=document.createElement("style"),d.id=e;
var _=/url\s*\(\s*\/(\"(?:[^\\\"\r\n\f]|\\[\s\S])*\"|'(?:[^\\'\n\r\f]|\\[\s\S])*'|[^)}]+)\s*\)/g,l=window.testenv_reshost||window.__moon_host||"res.wx.qq.com";
t=t.replace(_,"url(//"+l+"/$1)"),d.innerHTML=t,document.getElementsByTagName("head")[0].appendChild(d);
}
}
return t;
};
e.combo_status=e.COMBO_UNLOAD,e.run=function(){
var o=e.run.info,n=o&&o[0],t=o&&o[1];
if(n&&e.combo_status==e.COMBO_LOADED){
var r=i(n);
t&&t(r);
}
},e.use=function(o,n){
window.__wxgspeeds&&(window.__wxgspeeds.seajs_use_time=+new Date),e.run.info=[o,n],
e.run();
},window.define=t,window.seajs=e;
}(),function(){
if(window.__nonce_str){
var e=document.createElement;
document.createElement=function(o){
var n=e.apply(this,arguments);
return"object"==typeof o&&(o=o.toString()),"string"==typeof o&&"script"==o.toLowerCase()&&n.setAttribute("nonce",window.__nonce_str),
n;
};
}
window.addEventListener&&window.__DEBUGINFO&&Math.random()<.01&&window.addEventListener("load",function(){
var e=document.createElement("script");
e.src=__DEBUGINFO.safe_js,e.type="text/javascript",e.async=!0;
var o=document.head||document.getElementsByTagName("head")[0];
o.appendChild(e);
});
}(),function(){
function n(e){
return"[object Array]"===Object.prototype.toString.call(e);
}
function t(e){
return"[object Object]"===Object.prototype.toString.call(e);
}
function r(e){
var n=e.stack+" "+e.toString()||"";
try{
if(window.testenv_reshost){
var t="http(s)?://"+window.testenv_reshost,r=new RegExp(t,"g");
n=n.replace(r,"");
}else n=n.replace(/http(s)?:\/\/res\.wx\.qq\.com/g,"");
for(var r=/\/([^.]+)\/js\/(\S+?)\.js(\,|:)?/g;r.test(n);)n=n.replace(r,function(e,o,n,t){
return n+t;
});
}catch(e){
n=e.stack?e.stack:"";
}
var i=[];
for(o in m)m.hasOwnProperty(o)&&i.push(o+":"+m[o]);
return i.push("STK:"+n.replace(/\n/g,"")),i.join("|");
}
function i(e,o,n){
if(!/^mp\.weixin\.qq\.com$/.test(location.hostname)){
var t=[];
n=n.replace(location.href,(location.origin||"")+(location.pathname||"")).replace("#wechat_redirect","").replace("#rd","").split("&");
for(var r=0,i=n.length;i>r;r++){
var a=n[r].split("=");
a[0]&&a[1]&&t.push(a[0]+"="+encodeURIComponent(a[1]));
}
var s=new window.Image;
return void(s.src=(o+t.join("&")).substr(0,1024));
}
var c;
if(window.ActiveXObject)try{
c=new ActiveXObject("Msxml2.XMLHTTP");
}catch(d){
try{
c=new ActiveXObject("Microsoft.XMLHTTP");
}catch(_){
c=!1;
}
}else window.XMLHttpRequest&&(c=new XMLHttpRequest);
c&&(c.open(e,o,!0),c.setRequestHeader("cache-control","no-cache"),c.setRequestHeader("Content-Type","application/x-www-form-urlencoded; charset=UTF-8"),
c.setRequestHeader("X-Requested-With","XMLHttpRequest"),c.send(n));
}
function a(e){
return function(o,n){
if("string"==typeof o)try{
o=new Function(o);
}catch(t){
throw t;
}
var r=[].slice.call(arguments,2),i=o;
return o=function(){
try{
return i.apply(this,r.length&&r||arguments);
}catch(e){
throw e.stack&&console&&console.error&&console.error("[TryCatch]"+e.stack),h&&window.__moon_report&&window.__moon_report([{
offset:O,
log:"timeout_error;host:"+location.host,
e:e
}]),e;
}
},e(o,n);
};
}
function s(e){
return function(o,n,t){
if("undefined"==typeof t)var t=!1;
var r=this,i=n||function(){};
return n=function(){
try{
return i.apply(r,arguments);
}catch(e){
throw e.stack&&console&&console.error&&console.error("[TryCatch]"+e.stack),h&&window.__moon_report&&window.__moon_report([{
offset:v,
log:"listener_error;type:"+o+";host:"+location.host,
e:e
}]),e;
}
},i.moon_lid=j,x[j]=n,j++,e.call(r,o,n,t);
};
}
function c(e){
return function(o,n,t){
if("undefined"==typeof t)var t=!1;
var r=this;
return n=x[n.moon_lid],e.call(r,o,n,t);
};
}
var d,_,l,m,w,u=/MicroMessenger/i.test(navigator.userAgent),f=/MPAPP/i.test(navigator.userAgent),p=window.define,h=121261,g=0,v=2,y=4,O=9,E=10;
if(window.__initCatch=function(e){
h=e.idkey,d=e.startKey||0,_=e.limit,l=e.badjsId,m=e.reportOpt||"",w=e.extInfo||{},
w.rate=w.rate||.5;
},window.__moon_report=function(e,o){
var a=!1,s="";
try{
s=top.location.href;
}catch(c){
a=!0;
}
var m=.5;
if(w&&w.rate&&(m=w.rate),o&&"number"==typeof o&&(m=o),!/mp\.weixin\.qq\.com/.test(location.href)&&!/payapp\.weixin\.qq\.com/.test(location.href)||Math.random()>m||!u&&!f||top!=window&&!a&&!/mp\.weixin\.qq\.com/.test(s),
t(e)&&(e=[e]),n(e)&&""!=h){
var p="",g=[],v=[],O=[],E=[];
"number"!=typeof _&&(_=1/0);
for(var x=0;x<e.length;x++){
var j=e[x]||{};
if(!(j.offset>_||"number"!=typeof j.offset||j.offset==y&&w&&w.network_rate&&Math.random()>=w.network_rate)){
var b=1/0==_?d:d+j.offset;
g[x]="[moon]"+h+"_"+b+";"+j.log+";"+r(j.e||{})||"",v[x]=b,O[x]=1;
}
}
for(var D=0;D<v.length;D++)E[D]=h+"_"+v[D]+"_"+O[D],p=p+"&log"+D+"="+g[D];
if(E.length>0){
i("POST",location.protocol+"//mp.weixin.qq.com/mp/jsmonitor?","idkey="+E.join(";")+"&r="+Math.random()+"&lc="+g.length+p);
var m=1;
if(w&&w.badjs_rate&&(m=w.badjs_rate),Math.random()<m){
if(p=p.replace(/uin\:(.)*\|biz\:(.)*\|mid\:(.)*\|idx\:(.)*\|sn\:(.)*\|/,""),l){
var B=new Image,S="https://badjs.weixinbridge.com/badjs?id="+l+"&level=4&from="+encodeURIComponent(location.host)+"&msg="+encodeURIComponent(p);
B.src=S.slice(0,1024);
}
if("undefined"!=typeof WX_BJ_REPORT&&WX_BJ_REPORT.BadJs)for(var x=0;x<e.length;x++){
var j=e[x]||{};
if(j.e)WX_BJ_REPORT.BadJs.onError(j.e);else{
var I=/[^:;]*/.exec(j.log)[0];
WX_BJ_REPORT.BadJs.report(I,j.log,{
mid:"mmbizwap:Monitor"
});
}
}
}else for(var x=0;x<e.length;x++){
var j=e[x]||{};
j.e&&(j.e.BADJS_EXCUTED=!0);
}
}
}
},window.setTimeout=a(window.setTimeout),window.setInterval=a(window.setInterval),
Math.random()<.01&&window.Document&&window.HTMLElement){
var x={},j=0;
Document.prototype.addEventListener=s(Document.prototype.addEventListener),Document.prototype.removeEventListener=c(Document.prototype.removeEventListener),
HTMLElement.prototype.addEventListener=s(HTMLElement.prototype.addEventListener),
HTMLElement.prototype.removeEventListener=c(HTMLElement.prototype.removeEventListener);
}
var b=window.navigator.userAgent;
if((/ip(hone|ad|od)/i.test(b)||/android/i.test(b))&&!/windows phone/i.test(b)&&window.localStorage&&window.localStorage.setItem){
var D=window.localStorage.setItem,B=0;
window.localStorage.setItem=function(e,o){
if(!(B>=10))try{
D.call(window.localStorage,e,o);
}catch(n){
n.stack&&console&&console.error&&console.error("[TryCatch]"+n.stack),window.__moon_report([{
offset:E,
log:"localstorage_error;"+n.toString(),
e:n
}]),B++,B>=3&&window.moon&&window.moon.clear&&moon.clear();
}
};
}
window.seajs&&p&&(window.define=function(){
for(var o,n=[],t=arguments&&arguments[0],i=0,a=arguments.length;a>i;i++){
var s=o=arguments[i];
"function"==typeof o&&(o=function(){
try{
return s.apply(this,arguments);
}catch(o){
throw"string"==typeof t&&console.error("[TryCatch][DefineeErr]id:"+t),o.stack&&console&&console.error&&console.error("[TryCatch]"+o.stack),
h&&window.__moon_report&&window.__moon_report([{
offset:g,
log:"define_error;id:"+t+";",
e:o
}]),e(" [define_error]"+JSON.stringify(r(o))),o;
}
},o.toString=function(e){
return function(){
return e.toString();
};
}(arguments[i])),n.push(o);
}
return p.apply(this,n);
});
}(),function(o){
function n(e,o,n){
return window.__DEBUGINFO?(window.__DEBUGINFO.res_list||(window.__DEBUGINFO.res_list=[]),
window.__DEBUGINFO.res_list[e]?(window.__DEBUGINFO.res_list[e][o]=n,!0):!1):!1;
}
function t(e){
var o=new TextEncoder("utf-8").encode(e),n=crypto.subtle||crypto.webkitSubtle;
return n.digest("SHA-256",o).then(function(e){
return r(e);
});
}
function r(e){
for(var o=[],n=new DataView(e),t=0;t<n.byteLength;t+=4){
var r=n.getUint32(t),i=r.toString(16),a="00000000",s=(a+i).slice(-a.length);
o.push(s);
}
return o.join("");
}
function i(e,o,n){
if("object"==typeof e){
var t=Object.prototype.toString.call(e).replace(/^\[object (.+)\]$/,function(e,o){
return o;
});
if(n=n||e,"Array"==t){
for(var r=0,i=e.length;i>r;++r)if(o.call(n,e[r],r,e)===!1)return;
}else{
if("Object"!==t&&a!=e)throw"unsupport type";
if(a==e){
for(var r=e.length-1;r>=0;r--){
var s=a.key(r),c=a.getItem(s);
if(o.call(n,c,s,e)===!1)return;
}
return;
}
for(var r in e)if(e.hasOwnProperty(r)&&o.call(n,e[r],r,e)===!1)return;
}
}
}
var a=o.localStorage,s=document.head||document.getElementsByTagName("head")[0],c=1,d=11,_=12,l=13,m=window.__allowLoadResFromMp?1:2,w=window.__allowLoadResFromMp?1:0,u=m+w,f=window.testenv_reshost||window.__moon_host||"res.wx.qq.com",p=new RegExp("^(http(s)?:)?//"+f);
window.__loadAllResFromMp&&(f="mp.weixin.qq.com",m=0,u=m+w);
var h={
prefix:"__MOON__",
loaded:[],
unload:[],
clearSample:!0,
hit_num:0,
mod_num:0,
version:1003,
cacheData:{
js_mod_num:0,
js_hit_num:0,
js_not_hit_num:0,
js_expired_num:0,
css_mod_num:0,
css_hit_num:0,
css_not_hit_num:0,
css_expired_num:0
},
init:function(){
h.loaded=[],h.unload=[];
var e,n,r;
if(window.no_moon_ls&&(h.clearSample=!0),a){
var s="_moon_ver_key_",c=a.getItem(s);
c!=h.version&&(h.clear(),a.setItem(s,h.version));
}
if((-1!=location.search.indexOf("no_moon1=1")||-1!=location.search.indexOf("no_lshttps=1"))&&h.clear(),
a){
var d=1*a.getItem(h.prefix+"clean_time"),_=+new Date;
if(_-d>=1296e6){
h.clear();
try{
!!a&&a.setItem(h.prefix+"clean_time",+new Date);
}catch(l){}
}
}
i(moon_map,function(i,s){
if(n=h.prefix+s,r=!!i&&i.replace(p,""),e=!!a&&a.getItem(n),version=!!a&&(a.getItem(n+"_ver")||"").replace(p,""),
h.mod_num++,r&&-1!=r.indexOf(".css")?h.cacheData.css_mod_num++:r&&-1!=r.indexOf(".js")&&h.cacheData.js_mod_num++,
h.clearSample||!e||r!=version)h.unload.push(r.replace(p,"")),r&&-1!=r.indexOf(".css")?e?r!=version&&h.cacheData.css_expired_num++:h.cacheData.css_not_hit_num++:r&&-1!=r.indexOf(".js")&&(e?r!=version&&h.cacheData.js_expired_num++:h.cacheData.js_not_hit_num++);else{
if("https:"==location.protocol&&window.moon_hash_map&&window.moon_hash_map[s]&&window.crypto)try{
t(e).then(function(e){
window.moon_hash_map[s]!=e&&console.log(s);
});
}catch(c){}
try{
var d="//# sourceURL="+s+"\n//@ sourceURL="+s;
o.eval.call(o,'define("'+s+'",[],'+e+")"+d),h.hit_num++,r&&-1!=r.indexOf(".css")?h.cacheData.css_hit_num++:r&&-1!=r.indexOf(".js")&&h.cacheData.js_hit_num++;
}catch(c){
h.unload.push(r.replace(p,""));
}
}
}),h.load(h.genUrl());
},
genUrl:function(){
var e=h.unload;
if(!e||e.length<=0)return[];
var o,n,t="",r=[],i={},a=-1!=location.search.indexOf("no_moon2=1"),s="//"+f;
-1!=location.href.indexOf("moon_debug2=1")&&(s="//mp.weixin.qq.com");
for(var c=0,d=e.length;d>c;++c){
/^\/(.*?)\//.test(e[c]);
var _=/^\/(.*?)\//.exec(e[c]);
_.length<2||!_[1]||(n=_[1],t=i[n],t?(o=t+","+e[c],o.length>1e3||a?(r.push(t+"?v="+h.version),
t=location.protocol+s+e[c],i[n]=t):(t=o,i[n]=t)):(t=location.protocol+s+e[c],i[n]=t));
}
for(var l in i)i.hasOwnProperty(l)&&r.push(i[l]);
return r;
},
load:function(e){
if(window.__wxgspeeds&&(window.__wxgspeeds.mod_num=h.mod_num,window.__wxgspeeds.hit_num=h.hit_num),
!e||e.length<=0)return seajs.combo_status=seajs.COMBO_LOADED,seajs.run(),console.debug&&console.debug("[moon] load js complete, all in cache, cost time : 0ms, total count : "+h.mod_num+", hit num: "+h.hit_num),
void window.__moonclientlog.push("[moon] load js complete, all in cache, cost time : 0ms, total count : "+h.mod_num+", hit num: "+h.hit_num);
seajs.combo_status=seajs.COMBO_LOADING;
var o=0,n=+new Date;
window.__wxgspeeds&&(window.__wxgspeeds.combo_times=[],window.__wxgspeeds.combo_times.push(n)),
i(e,function(t){
h.request(t,u,function(){
if(window.__wxgspeeds&&window.__wxgspeeds.combo_times.push(+new Date),o++,o==e.length){
var t=+new Date-n;
window.__wxgspeeds&&(window.__wxgspeeds.mod_downloadtime=t),seajs.combo_status=seajs.COMBO_LOADED,
seajs.run(),console.debug&&console.debug("[moon] load js complete, url num : "+e.length+", total mod count : "+h.mod_num+", hit num: "+h.hit_num+", use time : "+t+"ms"),
window.__moonclientlog.push("[moon] load js complete, url num : "+e.length+", total mod count : "+h.mod_num+", hit num: "+h.hit_num+", use time : "+t+"ms");
}
});
});
},
request:function(o,t,r){
if(o){
t=t||0,o.indexOf("mp.weixin.qq.com")>-1&&((new Image).src=location.protocol+"//mp.weixin.qq.com/mp/jsmonitor?idkey=27613_32_1&r="+Math.random(),
window.__moon_report([{
offset:_,
log:"load_script_from_mp: "+o
}],1));
var i=-1;
window.__DEBUGINFO&&(__DEBUGINFO.res_list||(__DEBUGINFO.res_list=[]),__DEBUGINFO.res_list.push({
type:"js",
status:"pendding",
start:+new Date,
end:0,
url:o
}),i=__DEBUGINFO.res_list.length-1),-1!=location.search.indexOf("no_lshttps=1")&&(o=o.replace("http://","https://"));
var a=document.createElement("script");
a.src=o,a.type="text/javascript",a.async=!0,a.down_time=+new Date,a.onerror=function(s){
n(i,"status","error"),n(i,"end",+new Date);
var _=new Error(s);
if(t>=0)if(w>t){
var m=o.replace("res.wx.qq.com","mp.weixin.qq.com");
h.request(m,t,r);
}else h.request(o,t,r);else window.__moon_report&&window.__moon_report([{
offset:c,
log:"load_script_error: "+o,
e:_
}],1);
if(t==w-1&&window.__moon_report([{
offset:d,
log:"load_script_error: "+o,
e:_
}],1),-1==t){
var u="ua: "+window.navigator.userAgent+", time="+(+new Date-a.down_time)+", load_script_error -1 : "+o;
window.__moon_report([{
offset:l,
log:u
}],1);
}
window.__moonclientlog.push("moon load js error : "+o+", error -> "+_.toString()),
e("moon_request_error url:"+o);
},"undefined"!=typeof moon_crossorigin&&moon_crossorigin&&a.setAttribute("crossorigin",!0),
a.onload=a.onreadystatechange=function(){
n(i,"status","loaded"),n(i,"end",+new Date),!a||a.readyState&&!/loaded|complete/.test(a.readyState)||(n(i,"status","200"),
a.onload=a.onreadystatechange=null,"function"==typeof r&&r());
},t--,s.appendChild(a),e("moon_request url:"+o+" retry:"+t);
}
},
setItem:function(e,o){
!!a&&a.setItem(e,o);
},
clear:function(){
a&&(i(a,function(e,o){
~o.indexOf(h.prefix)&&a.removeItem(o);
}),console.debug&&console.debug("[moon] clear"));
},
idkeyReport:function(e,o,n){
n=n||1;
var t=e+"_"+o+"_"+n;
(new Image).src="/mp/jsmonitor?idkey="+t+"&r="+Math.random();
}
};
seajs&&seajs.use&&"string"==typeof window.__moon_mainjs&&seajs.use(window.__moon_mainjs),
window.moon=h;
}(window),function(){
try{
Math.random()<1;
}catch(e){}
}(),window.moon.init();
};
e(),!!window.__moon_initcallback&&window.__moon_initcallback(),window.__wxgspeeds&&(window.__wxgspeeds.moonendtime=+new Date);
}
}
var WX_BJ_REPORT=window.WX_BJ_REPORT||{};
!function(e){
function o(e,o,n,t,r,i){
return{
name:e||"",
message:o||"",
file:n||"",
line:t||"",
col:r||"",
stack:i&&i.stack||""
};
}
function n(e){
var o=t(e);
return{
name:e.name,
key:e.message,
msg:e.message,
stack:o.info,
file:o.file,
line:o.line,
col:o.col,
client_version:"",
_info:e._info
};
}
function t(o){
o._info=o._info||"";
var n=o.stack||"",t={
info:n,
file:o.file||"",
line:o.line||"",
col:o.col||""
};
if(""==t.file){
var r=n.split(/\bat\b/);
if(r&&r[1]){
var i=/(https?:\/\/[^\n]+)\:(\d+)\:(\d+)/.exec(r[1]);
i&&(i[1]&&i[1]!=t.file&&(t.file&&(o._info+=" [file: "+t.file+" ]"),t.file=i[1]),
i[2]&&i[2]!=t.line&&(t.line&&(o._info+=" [line: "+t.line+" ]"),t.line=i[2]),i[3]&&i[3]!=t.col&&(t.col&&(o._info+=" [col: "+t.col+" ]"),
t.col=i[3]));
}
}
return t&&t.file&&t.file.length>0&&(t.info=t.info.replace(new RegExp(t.file.split("?")[0],"gi"),"__FILE__")),
e.BadJs.ignorePath&&(t.info=t.info.replace(/http(s)?\:[^:\n]*\//gi,"").replace(/\n/gi,"")),
t;
}
if(!e.BadJs){
var r="BadjsWindowError",i=function(e,o){
for(var n in o)e[n]=o[n];
return e;
};
return e.BadJs={
uin:0,
mid:"",
view:"wap",
_cache:{},
_info:{},
_hookCallback:null,
ignorePath:!0,
"throw":function(e,o){
throw this.onError(e,o),e;
},
onError:function(o,t){
try{
if(1==o.BADJS_EXCUTED)return;
o.BADJS_EXCUTED=!0;
var r=n(o);
if(r.uin=this.uin,r.mid=this.mid,r.view=this.view,r.cmdb_module="mmbizwap",t&&(r=i(r,t)),
r.cid&&(r.key="["+r.cid+"]:"+r.key),o._info&&(r.msg+=" || e.info:"+o._info),"{}"!=JSON.stringify(this._info)&&(r.msg+=" || info:"+JSON.stringify(this._info)),
"function"==typeof this._hookCallback&&this._hookCallback(r)===!1)return;
return this._send(r),e.BadJs;
}catch(o){
console.error(o);
}
},
winErr:function(n){
n.error&&n.error.BADJS_EXCUTED||e.BadJs.onError(o(r,n.message,n.filename,n.lineno,n.colno,n.error));
},
init:function(o,n,t){
return this.uin=o||this.uin,this.mid=n||this.mid,this.view=t||this.view,e.BadJs;
},
hook:function(o){
return this._hookCallback=o,e.BadJs;
},
_send:function(o){
if(!o.mid){
if("undefined"==typeof window.PAGE_MID||!window.PAGE_MID)return;
o.mid=window.PAGE_MID;
}
o.uin||(o.uin=window.user_uin||0);
var n=[o.mid,o.name,o.key].join("|");
if(!this._cache||!this._cache[n])return this._cache&&(this._cache[n]=!0),this._xhr(o),
e.BadJs;
},
_xhr:function(e){
var o;
if(window.ActiveXObject)try{
o=new ActiveXObject("Msxml2.XMLHTTP");
}catch(n){
try{
o=new ActiveXObject("Microsoft.XMLHTTP");
}catch(t){
o=!1;
}
}else window.XMLHttpRequest&&(o=new XMLHttpRequest);
var r="";
for(var i in e)i&&e[i]&&(r+=[i,"=",encodeURIComponent(e[i]),"&"].join(""));
if(o&&o.open)o.open("POST","https://badjs.weixinbridge.com/report",!0),o.setRequestHeader("Content-Type","application/x-www-form-urlencoded; charset=UTF-8"),
o.onreadystatechange=function(){},o.send(r.slice(0,-1));else{
var a=new Image;
a.src="https://badjs.weixinbridge.com/report?"+r;
}
},
report:function(e,n,t){
return this.onError(o(e,n),t),this;
},
mark:function(e){
this._info=i(this._info,e);
},
nocache:function(){
return this._cache=!1,e.BadJs;
}
},window.addEventListener&&window.addEventListener("error",e.BadJs.winErr),e.BadJs;
}
}(WX_BJ_REPORT),window.WX_BJ_REPORT=WX_BJ_REPORT,__moonf__(); }, 25);</script><script nonce="567503264">
    
    (function() {
        var ua = navigator.userAgent;
        if (ua.indexOf("MicroMessenger") != -1 && ua.indexOf("Android") != -1){
            var script = document.createElement('script');
            var head = document.getElementsByTagName('head')[0];
            script.type = 'text/javascript';
            script.src = "https://midas.gtimg.cn/h5sdk/js/api/h5sdk.js";
            head.appendChild(script);
        }
    })();
</script>
<script nonce="567503264" type="text/javascript">
    var real_show_page_time = +new Date();
    if (!!window.addEventListener){
        window.addEventListener("load", function(){
            window.onload_endtime = +new Date();
        });
    }
    
    
</script>

    </body>
</html>

"""

resp_obj = BeautifulSoup(aaa, 'html.parser')
bb = [s.extract() for s in resp_obj("iframe")]
print(bb)
article_text = resp_obj.find("div", attrs={"id": "js_content"}).text.strip()
print(article_text)