"use strict";(self.webpackChunkvoice_over_front=self.webpackChunkvoice_over_front||[]).push([[182],{1182:(ye,M,s)=>{s.r(M),s.d(M,{SttModule:()=>ve});var g=s(9808),C=s(1787),e=s(4893),P=s(4594);const N=["audioInput"],U=["audioPlayer"];let Y=(()=>{class n{constructor(){this.audio=new e.vpe}_updateAudioPlayer(t){!this.audioPlayer||(this.audioPlayer.nativeElement.src=t.target.result,this.audioPlayer.nativeElement.load())}reset(){this.audioInput&&(this.audioInput.nativeElement.value=""),this.audioPlayer&&(this.audioPlayer.nativeElement.src=""),this.audio.emit(null)}onSelectAudio(){if(!this.audioInput)return;const t=this.audioInput.nativeElement.files;if(!t||0===t.length)return;const i=t[0];if(!i)return;this.audio.emit(i);const a=new FileReader;a.onload=this._updateAudioPlayer.bind(this),a.readAsDataURL(i)}}return n.\u0275fac=function(t){return new(t||n)},n.\u0275cmp=e.Xpm({type:n,selectors:[["app-audio"]],viewQuery:function(t,i){if(1&t&&(e.Gf(N,5),e.Gf(U,5)),2&t){let a;e.iGM(a=e.CRH())&&(i.audioInput=a.first),e.iGM(a=e.CRH())&&(i.audioPlayer=a.first)}},outputs:{audio:"audio"},decls:5,vars:0,consts:[["id","content"],["type","file","accept","audio/wav","title","Select an audio file",1,"mb-3",3,"change"],["audioInput",""],["controls",""],["audioPlayer",""]],template:function(t,i){1&t&&(e.TgZ(0,"div",0),e.TgZ(1,"input",1,2),e.NdJ("change",function(){return i.onSelectAudio()}),e.qZA(),e._UZ(3,"audio",3,4),e.qZA())},styles:["[_nghost-%COMP%]{display:block}[_nghost-%COMP%]   audio[_ngcontent-%COMP%]{width:100%}"]}),n})();var T=s(4106),E=s(4107),b=s(508),S=s(7423),J=s(5861),Q=s(4464),j=s(5830),u=s(3191),m=s(7579),w=s(727),H=s(449);let G=0;const v=new e.OlP("CdkAccordion");let L=(()=>{class n{constructor(){this._stateChanges=new m.x,this._openCloseAllActions=new m.x,this.id="cdk-accordion-"+G++,this._multi=!1}get multi(){return this._multi}set multi(t){this._multi=(0,u.Ig)(t)}openAll(){this._multi&&this._openCloseAllActions.next(!0)}closeAll(){this._openCloseAllActions.next(!1)}ngOnChanges(t){this._stateChanges.next(t)}ngOnDestroy(){this._stateChanges.complete(),this._openCloseAllActions.complete()}}return n.\u0275fac=function(t){return new(t||n)},n.\u0275dir=e.lG2({type:n,selectors:[["cdk-accordion"],["","cdkAccordion",""]],inputs:{multi:"multi"},exportAs:["cdkAccordion"],features:[e._Bn([{provide:v,useExisting:n}]),e.TTD]}),n})(),z=0,X=(()=>{class n{constructor(t,i,a){this.accordion=t,this._changeDetectorRef=i,this._expansionDispatcher=a,this._openCloseAllSubscription=w.w0.EMPTY,this.closed=new e.vpe,this.opened=new e.vpe,this.destroyed=new e.vpe,this.expandedChange=new e.vpe,this.id="cdk-accordion-child-"+z++,this._expanded=!1,this._disabled=!1,this._removeUniqueSelectionListener=()=>{},this._removeUniqueSelectionListener=a.listen((d,l)=>{this.accordion&&!this.accordion.multi&&this.accordion.id===l&&this.id!==d&&(this.expanded=!1)}),this.accordion&&(this._openCloseAllSubscription=this._subscribeToOpenCloseAllActions())}get expanded(){return this._expanded}set expanded(t){t=(0,u.Ig)(t),this._expanded!==t&&(this._expanded=t,this.expandedChange.emit(t),t?(this.opened.emit(),this._expansionDispatcher.notify(this.id,this.accordion?this.accordion.id:this.id)):this.closed.emit(),this._changeDetectorRef.markForCheck())}get disabled(){return this._disabled}set disabled(t){this._disabled=(0,u.Ig)(t)}ngOnDestroy(){this.opened.complete(),this.closed.complete(),this.destroyed.emit(),this.destroyed.complete(),this._removeUniqueSelectionListener(),this._openCloseAllSubscription.unsubscribe()}toggle(){this.disabled||(this.expanded=!this.expanded)}close(){this.disabled||(this.expanded=!1)}open(){this.disabled||(this.expanded=!0)}_subscribeToOpenCloseAllActions(){return this.accordion._openCloseAllActions.subscribe(t=>{this.disabled||(this.expanded=t)})}}return n.\u0275fac=function(t){return new(t||n)(e.Y36(v,12),e.Y36(e.sBO),e.Y36(H.A8))},n.\u0275dir=e.lG2({type:n,selectors:[["cdk-accordion-item"],["","cdkAccordionItem",""]],inputs:{expanded:"expanded",disabled:"disabled"},outputs:{closed:"closed",opened:"opened",destroyed:"destroyed",expandedChange:"expandedChange"},exportAs:["cdkAccordionItem"],features:[e._Bn([{provide:v,useValue:void 0}])]}),n})(),V=(()=>{class n{}return n.\u0275fac=function(t){return new(t||n)},n.\u0275mod=e.oAB({type:n}),n.\u0275inj=e.cJS({}),n})();var y=s(7429),D=s(5664),q=s(1884),Z=s(8675),f=s(9300),$=s(5698),_=s(1159),I=s(6360),K=s(515),W=s(6451),r=s(1777);const ee=["body"];function te(n,o){}const ne=[[["mat-expansion-panel-header"]],"*",[["mat-action-row"]]],ie=["mat-expansion-panel-header","*","mat-action-row"];function oe(n,o){if(1&n&&e._UZ(0,"span",2),2&n){const t=e.oxw();e.Q6J("@indicatorRotate",t._getExpandedState())}}const ae=[[["mat-panel-title"]],[["mat-panel-description"]],"*"],se=["mat-panel-title","mat-panel-description","*"],A=new e.OlP("MAT_ACCORDION"),O="225ms cubic-bezier(0.4,0.0,0.2,1)",k={indicatorRotate:(0,r.X$)("indicatorRotate",[(0,r.SB)("collapsed, void",(0,r.oB)({transform:"rotate(0deg)"})),(0,r.SB)("expanded",(0,r.oB)({transform:"rotate(180deg)"})),(0,r.eR)("expanded <=> collapsed, void => collapsed",(0,r.jt)(O))]),bodyExpansion:(0,r.X$)("bodyExpansion",[(0,r.SB)("collapsed, void",(0,r.oB)({height:"0px",visibility:"hidden"})),(0,r.SB)("expanded",(0,r.oB)({height:"*",visibility:"visible"})),(0,r.eR)("expanded <=> collapsed, void => collapsed",(0,r.jt)(O))])};let de=(()=>{class n{constructor(t){this._template=t}}return n.\u0275fac=function(t){return new(t||n)(e.Y36(e.Rgc))},n.\u0275dir=e.lG2({type:n,selectors:[["ng-template","matExpansionPanelContent",""]]}),n})(),re=0;const B=new e.OlP("MAT_EXPANSION_PANEL_DEFAULT_OPTIONS");let R=(()=>{class n extends X{constructor(t,i,a,d,l,h,x){super(t,i,a),this._viewContainerRef=d,this._animationMode=h,this._hideToggle=!1,this.afterExpand=new e.vpe,this.afterCollapse=new e.vpe,this._inputChanges=new m.x,this._headerId="mat-expansion-panel-header-"+re++,this._bodyAnimationDone=new m.x,this.accordion=t,this._document=l,this._bodyAnimationDone.pipe((0,q.x)((c,p)=>c.fromState===p.fromState&&c.toState===p.toState)).subscribe(c=>{"void"!==c.fromState&&("expanded"===c.toState?this.afterExpand.emit():"collapsed"===c.toState&&this.afterCollapse.emit())}),x&&(this.hideToggle=x.hideToggle)}get hideToggle(){return this._hideToggle||this.accordion&&this.accordion.hideToggle}set hideToggle(t){this._hideToggle=(0,u.Ig)(t)}get togglePosition(){return this._togglePosition||this.accordion&&this.accordion.togglePosition}set togglePosition(t){this._togglePosition=t}_hasSpacing(){return!!this.accordion&&this.expanded&&"default"===this.accordion.displayMode}_getExpandedState(){return this.expanded?"expanded":"collapsed"}toggle(){this.expanded=!this.expanded}close(){this.expanded=!1}open(){this.expanded=!0}ngAfterContentInit(){this._lazyContent&&this.opened.pipe((0,Z.O)(null),(0,f.h)(()=>this.expanded&&!this._portal),(0,$.q)(1)).subscribe(()=>{this._portal=new y.UE(this._lazyContent._template,this._viewContainerRef)})}ngOnChanges(t){this._inputChanges.next(t)}ngOnDestroy(){super.ngOnDestroy(),this._bodyAnimationDone.complete(),this._inputChanges.complete()}_containsFocus(){if(this._body){const t=this._document.activeElement,i=this._body.nativeElement;return t===i||i.contains(t)}return!1}}return n.\u0275fac=function(t){return new(t||n)(e.Y36(A,12),e.Y36(e.sBO),e.Y36(H.A8),e.Y36(e.s_b),e.Y36(g.K0),e.Y36(I.Qb,8),e.Y36(B,8))},n.\u0275cmp=e.Xpm({type:n,selectors:[["mat-expansion-panel"]],contentQueries:function(t,i,a){if(1&t&&e.Suo(a,de,5),2&t){let d;e.iGM(d=e.CRH())&&(i._lazyContent=d.first)}},viewQuery:function(t,i){if(1&t&&e.Gf(ee,5),2&t){let a;e.iGM(a=e.CRH())&&(i._body=a.first)}},hostAttrs:[1,"mat-expansion-panel"],hostVars:6,hostBindings:function(t,i){2&t&&e.ekj("mat-expanded",i.expanded)("_mat-animation-noopable","NoopAnimations"===i._animationMode)("mat-expansion-panel-spacing",i._hasSpacing())},inputs:{disabled:"disabled",expanded:"expanded",hideToggle:"hideToggle",togglePosition:"togglePosition"},outputs:{opened:"opened",closed:"closed",expandedChange:"expandedChange",afterExpand:"afterExpand",afterCollapse:"afterCollapse"},exportAs:["matExpansionPanel"],features:[e._Bn([{provide:A,useValue:void 0}]),e.qOj,e.TTD],ngContentSelectors:ie,decls:7,vars:4,consts:[["role","region",1,"mat-expansion-panel-content",3,"id"],["body",""],[1,"mat-expansion-panel-body"],[3,"cdkPortalOutlet"]],template:function(t,i){1&t&&(e.F$t(ne),e.Hsn(0),e.TgZ(1,"div",0,1),e.NdJ("@bodyExpansion.done",function(d){return i._bodyAnimationDone.next(d)}),e.TgZ(3,"div",2),e.Hsn(4,1),e.YNc(5,te,0,0,"ng-template",3),e.qZA(),e.Hsn(6,2),e.qZA()),2&t&&(e.xp6(1),e.Q6J("@bodyExpansion",i._getExpandedState())("id",i.id),e.uIk("aria-labelledby",i._headerId),e.xp6(4),e.Q6J("cdkPortalOutlet",i._portal))},directives:[y.Pl],styles:[".mat-expansion-panel{box-sizing:content-box;display:block;margin:0;border-radius:4px;overflow:hidden;transition:margin 225ms cubic-bezier(0.4, 0, 0.2, 1),box-shadow 280ms cubic-bezier(0.4, 0, 0.2, 1);position:relative}.mat-accordion .mat-expansion-panel:not(.mat-expanded),.mat-accordion .mat-expansion-panel:not(.mat-expansion-panel-spacing){border-radius:0}.mat-accordion .mat-expansion-panel:first-of-type{border-top-right-radius:4px;border-top-left-radius:4px}.mat-accordion .mat-expansion-panel:last-of-type{border-bottom-right-radius:4px;border-bottom-left-radius:4px}.cdk-high-contrast-active .mat-expansion-panel{outline:solid 1px}.mat-expansion-panel.ng-animate-disabled,.ng-animate-disabled .mat-expansion-panel,.mat-expansion-panel._mat-animation-noopable{transition:none}.mat-expansion-panel-content{display:flex;flex-direction:column;overflow:visible}.mat-expansion-panel-body{padding:0 24px 16px}.mat-expansion-panel-spacing{margin:16px 0}.mat-accordion>.mat-expansion-panel-spacing:first-child,.mat-accordion>*:first-child:not(.mat-expansion-panel) .mat-expansion-panel-spacing{margin-top:0}.mat-accordion>.mat-expansion-panel-spacing:last-child,.mat-accordion>*:last-child:not(.mat-expansion-panel) .mat-expansion-panel-spacing{margin-bottom:0}.mat-action-row{border-top-style:solid;border-top-width:1px;display:flex;flex-direction:row;justify-content:flex-end;padding:16px 8px 16px 24px}.mat-action-row button.mat-button-base,.mat-action-row button.mat-mdc-button-base{margin-left:8px}[dir=rtl] .mat-action-row button.mat-button-base,[dir=rtl] .mat-action-row button.mat-mdc-button-base{margin-left:0;margin-right:8px}\n"],encapsulation:2,data:{animation:[k.bodyExpansion]},changeDetection:0}),n})(),le=(()=>{class n{}return n.\u0275fac=function(t){return new(t||n)},n.\u0275dir=e.lG2({type:n,selectors:[["mat-action-row"]],hostAttrs:[1,"mat-action-row"]}),n})();class pe{}const ce=(0,b.sb)(pe);let F=(()=>{class n extends ce{constructor(t,i,a,d,l,h,x){super(),this.panel=t,this._element=i,this._focusMonitor=a,this._changeDetectorRef=d,this._animationMode=h,this._parentChangeSubscription=w.w0.EMPTY;const c=t.accordion?t.accordion._stateChanges.pipe((0,f.h)(p=>!(!p.hideToggle&&!p.togglePosition))):K.E;this.tabIndex=parseInt(x||"")||0,this._parentChangeSubscription=(0,W.T)(t.opened,t.closed,c,t._inputChanges.pipe((0,f.h)(p=>!!(p.hideToggle||p.disabled||p.togglePosition)))).subscribe(()=>this._changeDetectorRef.markForCheck()),t.closed.pipe((0,f.h)(()=>t._containsFocus())).subscribe(()=>a.focusVia(i,"program")),l&&(this.expandedHeight=l.expandedHeight,this.collapsedHeight=l.collapsedHeight)}get disabled(){return this.panel.disabled}_toggle(){this.disabled||this.panel.toggle()}_isExpanded(){return this.panel.expanded}_getExpandedState(){return this.panel._getExpandedState()}_getPanelId(){return this.panel.id}_getTogglePosition(){return this.panel.togglePosition}_showToggle(){return!this.panel.hideToggle&&!this.panel.disabled}_getHeaderHeight(){const t=this._isExpanded();return t&&this.expandedHeight?this.expandedHeight:!t&&this.collapsedHeight?this.collapsedHeight:null}_keydown(t){switch(t.keyCode){case _.L_:case _.K5:(0,_.Vb)(t)||(t.preventDefault(),this._toggle());break;default:return void(this.panel.accordion&&this.panel.accordion._handleHeaderKeydown(t))}}focus(t,i){t?this._focusMonitor.focusVia(this._element,t,i):this._element.nativeElement.focus(i)}ngAfterViewInit(){this._focusMonitor.monitor(this._element).subscribe(t=>{t&&this.panel.accordion&&this.panel.accordion._handleHeaderFocus(this)})}ngOnDestroy(){this._parentChangeSubscription.unsubscribe(),this._focusMonitor.stopMonitoring(this._element)}}return n.\u0275fac=function(t){return new(t||n)(e.Y36(R,1),e.Y36(e.SBq),e.Y36(D.tE),e.Y36(e.sBO),e.Y36(B,8),e.Y36(I.Qb,8),e.$8M("tabindex"))},n.\u0275cmp=e.Xpm({type:n,selectors:[["mat-expansion-panel-header"]],hostAttrs:["role","button",1,"mat-expansion-panel-header","mat-focus-indicator"],hostVars:15,hostBindings:function(t,i){1&t&&e.NdJ("click",function(){return i._toggle()})("keydown",function(d){return i._keydown(d)}),2&t&&(e.uIk("id",i.panel._headerId)("tabindex",i.tabIndex)("aria-controls",i._getPanelId())("aria-expanded",i._isExpanded())("aria-disabled",i.panel.disabled),e.Udp("height",i._getHeaderHeight()),e.ekj("mat-expanded",i._isExpanded())("mat-expansion-toggle-indicator-after","after"===i._getTogglePosition())("mat-expansion-toggle-indicator-before","before"===i._getTogglePosition())("_mat-animation-noopable","NoopAnimations"===i._animationMode))},inputs:{tabIndex:"tabIndex",expandedHeight:"expandedHeight",collapsedHeight:"collapsedHeight"},features:[e.qOj],ngContentSelectors:se,decls:5,vars:1,consts:[[1,"mat-content"],["class","mat-expansion-indicator",4,"ngIf"],[1,"mat-expansion-indicator"]],template:function(t,i){1&t&&(e.F$t(ae),e.TgZ(0,"span",0),e.Hsn(1),e.Hsn(2,1),e.Hsn(3,2),e.qZA(),e.YNc(4,oe,1,1,"span",1)),2&t&&(e.xp6(4),e.Q6J("ngIf",i._showToggle()))},directives:[g.O5],styles:['.mat-expansion-panel-header{display:flex;flex-direction:row;align-items:center;padding:0 24px;border-radius:inherit;transition:height 225ms cubic-bezier(0.4, 0, 0.2, 1)}.mat-expansion-panel-header._mat-animation-noopable{transition:none}.mat-expansion-panel-header:focus,.mat-expansion-panel-header:hover{outline:none}.mat-expansion-panel-header.mat-expanded:focus,.mat-expansion-panel-header.mat-expanded:hover{background:inherit}.mat-expansion-panel-header:not([aria-disabled=true]){cursor:pointer}.mat-expansion-panel-header.mat-expansion-toggle-indicator-before{flex-direction:row-reverse}.mat-expansion-panel-header.mat-expansion-toggle-indicator-before .mat-expansion-indicator{margin:0 16px 0 0}[dir=rtl] .mat-expansion-panel-header.mat-expansion-toggle-indicator-before .mat-expansion-indicator{margin:0 0 0 16px}.mat-content{display:flex;flex:1;flex-direction:row;overflow:hidden}.mat-expansion-panel-header-title,.mat-expansion-panel-header-description{display:flex;flex-grow:1;margin-right:16px}[dir=rtl] .mat-expansion-panel-header-title,[dir=rtl] .mat-expansion-panel-header-description{margin-right:0;margin-left:16px}.mat-expansion-panel-header-description{flex-grow:2}.mat-expansion-indicator::after{border-style:solid;border-width:0 2px 2px 0;content:"";display:inline-block;padding:3px;transform:rotate(45deg);vertical-align:middle}.cdk-high-contrast-active .mat-expansion-panel .mat-expansion-panel-header.cdk-keyboard-focused:not([aria-disabled=true])::before,.cdk-high-contrast-active .mat-expansion-panel .mat-expansion-panel-header.cdk-program-focused:not([aria-disabled=true])::before,.cdk-high-contrast-active .mat-expansion-panel:not(.mat-expanded) .mat-expansion-panel-header:hover:not([aria-disabled=true])::before{top:0;left:0;right:0;bottom:0;position:absolute;box-sizing:border-box;pointer-events:none;border:3px solid;border-radius:4px;content:""}.cdk-high-contrast-active .mat-expansion-panel-content{border-top:1px solid;border-top-left-radius:0;border-top-right-radius:0}\n'],encapsulation:2,data:{animation:[k.indicatorRotate]},changeDetection:0}),n})(),ue=(()=>{class n{}return n.\u0275fac=function(t){return new(t||n)},n.\u0275dir=e.lG2({type:n,selectors:[["mat-panel-description"]],hostAttrs:[1,"mat-expansion-panel-header-description"]}),n})(),he=(()=>{class n{}return n.\u0275fac=function(t){return new(t||n)},n.\u0275dir=e.lG2({type:n,selectors:[["mat-panel-title"]],hostAttrs:[1,"mat-expansion-panel-header-title"]}),n})(),ge=(()=>{class n extends L{constructor(){super(...arguments),this._ownHeaders=new e.n_E,this._hideToggle=!1,this.displayMode="default",this.togglePosition="after"}get hideToggle(){return this._hideToggle}set hideToggle(t){this._hideToggle=(0,u.Ig)(t)}ngAfterContentInit(){this._headers.changes.pipe((0,Z.O)(this._headers)).subscribe(t=>{this._ownHeaders.reset(t.filter(i=>i.panel.accordion===this)),this._ownHeaders.notifyOnChanges()}),this._keyManager=new D.Em(this._ownHeaders).withWrap().withHomeAndEnd()}_handleHeaderKeydown(t){this._keyManager.onKeydown(t)}_handleHeaderFocus(t){this._keyManager.updateActiveItem(t)}ngOnDestroy(){super.ngOnDestroy(),this._ownHeaders.destroy()}}return n.\u0275fac=function(){let o;return function(i){return(o||(o=e.n5z(n)))(i||n)}}(),n.\u0275dir=e.lG2({type:n,selectors:[["mat-accordion"]],contentQueries:function(t,i,a){if(1&t&&e.Suo(a,F,5),2&t){let d;e.iGM(d=e.CRH())&&(i._headers=d)}},hostAttrs:[1,"mat-accordion"],hostVars:2,hostBindings:function(t,i){2&t&&e.ekj("mat-accordion-multi",i.multi)},inputs:{multi:"multi",hideToggle:"hideToggle",displayMode:"displayMode",togglePosition:"togglePosition"},exportAs:["matAccordion"],features:[e._Bn([{provide:A,useExisting:n}]),e.qOj]}),n})(),me=(()=>{class n{}return n.\u0275fac=function(t){return new(t||n)},n.\u0275mod=e.oAB({type:n}),n.\u0275inj=e.cJS({imports:[[g.ez,b.BQ,V,y.eL]]}),n})(),fe=(()=>{class n{constructor(t){this._sttService=t}reset(){this.transcription=void 0}update(){var t=this;return(0,J.Z)(function*(){if(!t.audio||!t.provider)return;const a=t._sttService.post_stt_single({data:t.audio,fileName:t.audio.name},t.provider,void 0);t.transcription=yield(0,Q.n)(a)})()}}return n.\u0275fac=function(t){return new(t||n)(e.Y36(j.qz))},n.\u0275cmp=e.Xpm({type:n,selectors:[["app-transcription-list"]],inputs:{audio:"audio",provider:"provider"},decls:12,vars:4,consts:[[1,"example-headers-align"],["expanded",""],[1,"mb-0"],[1,"badge","p-2","rounded-pill","bg-light","text-dark"]],template:function(t,i){if(1&t&&(e.TgZ(0,"mat-accordion",0),e.TgZ(1,"mat-expansion-panel",1),e.TgZ(2,"mat-expansion-panel-header"),e.TgZ(3,"mat-panel-title"),e._uU(4),e.qZA(),e.TgZ(5,"mat-panel-description"),e._uU(6),e.qZA(),e.qZA(),e.TgZ(7,"p",2),e._uU(8),e.qZA(),e.TgZ(9,"mat-action-row"),e.TgZ(10,"span",3),e._uU(11),e.qZA(),e.qZA(),e.qZA(),e.qZA()),2&t){let a;e.xp6(4),e.hij("Provider: ",null==i.transcription?null:i.transcription.provider,""),e.xp6(2),e.hij("Confidence: ",null==i.transcription?null:i.transcription.confidence,""),e.xp6(2),e.Oqu(null==i.transcription?null:i.transcription.transcription),e.xp6(3),e.hij("Execution time ",null!==(a=null==i.transcription?null:i.transcription.time)&&void 0!==a?a:0,"s")}},directives:[ge,R,F,he,ue,le],styles:["[_nghost-%COMP%]{display:block}"]}),n})();const xe=[{path:"",component:(()=>{class n{onAudioChange(t){this.selectedAudio=null!=t?t:void 0}onProviderChange(t){this.selectedProvider=t}}return n.\u0275fac=function(t){return new(t||n)},n.\u0275cmp=e.Xpm({type:n,selectors:[["app-stt-page"]],decls:22,vars:4,consts:[[1,"mb-3"],[1,"mb-3",3,"audio"],["audioSelector",""],["appearance","fill"],[3,"valueChange"],["value","rev"],["value","assembly"],["value","ibm"],["type","button","mat-raised-button","",1,"me-2",3,"disabled","click"],["type","button","mat-raised-button","",3,"disabled","click"],[3,"audio","provider"],["transcriptionList",""]],template:function(t,i){if(1&t){const a=e.EpF();e.TgZ(0,"mat-toolbar",0),e.TgZ(1,"span"),e._uU(2,"Speech to text"),e.qZA(),e.qZA(),e.TgZ(3,"app-audio",1,2),e.NdJ("audio",function(l){return i.onAudioChange(l)}),e.qZA(),e.TgZ(5,"mat-form-field",3),e.TgZ(6,"mat-label"),e._uU(7,"Provider"),e.qZA(),e.TgZ(8,"mat-select",4),e.NdJ("valueChange",function(l){return i.onProviderChange(l)}),e.TgZ(9,"mat-option",5),e._uU(10,"Rev.ai"),e.qZA(),e.TgZ(11,"mat-option",6),e._uU(12,"Assembly.ai"),e.qZA(),e.TgZ(13,"mat-option",7),e._uU(14,"IBM"),e.qZA(),e.qZA(),e.qZA(),e.TgZ(15,"div",0),e.TgZ(16,"button",8),e.NdJ("click",function(){return e.CHM(a),e.MAs(21).update()}),e._uU(17,"Transcript"),e.qZA(),e.TgZ(18,"button",9),e.NdJ("click",function(){e.CHM(a);const l=e.MAs(4),h=e.MAs(21);return l.reset(),h.reset()}),e._uU(19,"Reset"),e.qZA(),e.qZA(),e._UZ(20,"app-transcription-list",10,11)}2&t&&(e.xp6(16),e.Q6J("disabled",!i.selectedAudio||!i.selectedProvider),e.xp6(2),e.Q6J("disabled",!i.selectedAudio&&!i.selectedProvider),e.xp6(2),e.Q6J("audio",i.selectedAudio)("provider",i.selectedProvider))},directives:[P.Ye,Y,T.KE,T.hX,E.gD,b.ey,S.lW,fe],styles:["[_nghost-%COMP%]{display:block}"]}),n})()}];let be=(()=>{class n{}return n.\u0275fac=function(t){return new(t||n)},n.\u0275mod=e.oAB({type:n}),n.\u0275inj=e.cJS({imports:[[C.Bz.forChild(xe)],C.Bz]}),n})(),ve=(()=>{class n{}return n.\u0275fac=function(t){return new(t||n)},n.\u0275mod=e.oAB({type:n}),n.\u0275inj=e.cJS({imports:[[g.ez,be,P.g0,me,E.LD,S.ot]]}),n})()}}]);