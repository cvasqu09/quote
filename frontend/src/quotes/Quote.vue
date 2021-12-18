<template>
  <Card class="quote-card">
    <template #content>
      <ConfirmPopup></ConfirmPopup>
      <div class="p-d-flex p-jc-between">
        <span class="p-mr-3 quote-text">"{{ quote }}"</span>
        <transition name="fade">
          <i v-show="allowDelete" class="pi pi-trash trash-icon" @click="deleteQuote($event)"></i>
        </transition>
      </div>
    </template>
    <template #footer>
      <div class="p-d-flex p-jc-between">
        <span>
          <i class="pi pi-heart p-mr-1" v-bind:class="{'liked': liked_by_user}" @click="toggleLike()"></i>
          {{ like_count }}
        </span>
        <span class="quoter quote-text">-{{ quoter }}</span>
      </div>
    </template>
  </Card>
</template>

<script>
import {ref, toRefs} from "@vue/reactivity";
import http from "../utils/http";
import {useToast} from "primevue/usetoast";
import {StatusCodes} from "http-status-codes";
import {debounce} from "lodash";
import { useConfirm } from "primevue/useconfirm";

export default {
  name: "Quote",
  props: {
    id: {
      type: String,
      required: true,
    },
    liked_by_user: {
      type: Boolean,
      required: false,
      default: false
    },
    like_count: {
      type: Number,
      required: false,
      default: 0
    },
    quote: {
      type: String,
      required: true
    },
    quoter: {
      type: String,
      required: true,
      default: 'Unknown'
    },
    allowDelete: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  setup(props, {emit}) {
    const {quote, quoter, id} = toRefs(props)
    const showDeleteIcon = ref(false);
    const liked_by_user = ref(props.liked_by_user)
    const like_count = ref(props.like_count)
    const toastService = useToast();
    const confirm = useConfirm();

    const toggleShowDeleteIcon = () => {
      showDeleteIcon.value = (!showDeleteIcon.value && props.allowDelete)
    }
    const deleteQuote = (event) => {
      console.log('deleting quote')
      confirm.require({
        target: event.currentTarget,
        message: "Are you sure you want to delete?",
        icon: 'pi pi-trash',
        accept: async () => {
          try {
            await http.delete(`quote/${id.value}`);
            emit('delete')
          } catch (e) {
            console.log('error deleting', e);
          }
        },
        reject: () => {
          confirm.close()
        }
      })
    }
    const getLikeClass = () => {
      return liked_by_user.value ? 'liked' : null;
    }
    const toggleLike = debounce(async () => {
      try {
        const response = await http.post(`like/`, {quote: props.id})
        liked_by_user.value = !liked_by_user.value;
        if (response.status === StatusCodes.CREATED) {
          like_count.value += 1
        } else {
          like_count.value -= 1
        }
      } catch (e) {
        toastService.add({
          severity: 'error',
          summary: 'Error',
          detail: 'Error liking quote. Try again later.',
          life: 5000
        })
      }
    }, 200)

    return {
      quote,
      quoter,
      deleteQuote,
      showDeleteIcon,
      toggleShowDeleteIcon,
      getLikeClass,
      toggleLike,
      liked_by_user,
      like_count
    }
  }
}
</script>

<style lang="scss" scoped>
:deep(.p-card-body) {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.liked {
  color: red;
}

.fade-enter-from {
  opacity: 0
}

.fade-enter-to {
  opacity: 1
}

.fade-enter-active {
  transition: all 0.3s ease;
}

.fade-leave-from {
  opacity: 1;
}

.fade-leave-to {
  opacity: 0;
}

.fade-leave-active {
  transition: all 0.3s ease;
}

.trash-icon {
  &:hover {
    cursor: pointer;
  }
}

.quote-card {
  min-width: 200px;
  max-width: 500px;

  &:hover {
    cursor: pointer;
    box-shadow: 5px 5px 5px $gray-4;
  }
}

.quoter {
  font-style: italic;
}
</style>
