import {store} from '@/store/store'
import Cookies from 'js-cookie'

export function setCookies() {
    Cookies.set('account', store.account,)
    Cookies.set('username', store.username)
    Cookies.set('fullname', store.fullname)
    Cookies.set('phone', store.phone)
}

export function getCookies() {
    store.account = Cookies.get('account')
    store.username = Cookies.get('username')
    store.fullname = Cookies.get('fullname')
    store.phone = Cookies.get('phone')
}